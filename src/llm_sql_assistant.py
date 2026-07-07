from src.database import Database
from src.gemini_client import GeminiClient


class LLMSQLAssistant:

    def __init__(self):

        self.db = Database()

        self.gemini = GeminiClient()

    def get_schema_prompt(self):

        return """
You are a SQL expert.

Generate ONLY SQL.

Database Tables:

patients(
patient_id,
trial_id,
site_id,
gender,
age,
consent_date,
treatment_arm,
enrollment_status
)

trials(
trial_id,
phase,
therapeutic_area,
sponsor,
study_drug,
indication,
start_date,
planned_end_date,
trial_status,
target_enrollment
)

sites(
site_id,
trial_id,
site_name,
country,
country_code,
principal_investigator,
activation_date,
site_status
)

visits(
visit_id,
patient_id,
trial_id,
site_id,
visit_name,
visit_sequence,
scheduled_visit_date,
actual_visit_date,
visit_status
)

lab_results(
lab_result_id,
patient_id,
trial_id,
site_id,
visit_id,
test_name,
result_value,
unit,
normal_low,
normal_high,
result_flag,
collection_date
)

adverse_events(
ae_id,
patient_id,
trial_id,
site_id,
ae_term,
severity,
serious_flag,
related_to_study_drug,
reported_timestamp,
ae_status
)

drug_inventory(
inventory_id,
trial_id,
site_id,
drug_name,
batch_number,
quantity_available,
expiry_date,
inventory_snapshot_date
)

drug_shipments(
shipment_id,
trial_id,
site_id,
drug_name,
batch_number,
quantity_shipped,
shipment_sent_date,
shipment_received_date,
shipment_status
)

protocol_deviations(
deviation_id,
patient_id,
trial_id,
site_id,
visit_id,
deviation_type,
deviation_severity,
deviation_date,
deviation_status
)

reference_codes(
code_type,
code_value,
code_description
)

Rules:
1. Return ONLY SQL.
2. Use SELECT queries only.
3. Never use DELETE.
4. Never use UPDATE.
5. Never use DROP.
6. Never use INSERT.

IMPORTANT:

This database uses DuckDB.

Never use:
- DATABASE()
- SHOW DATABASES
- USE database_name
- INFORMATION_SCHEMA.SCHEMATA

Use DuckDB-compatible metadata tables:

information_schema.tables
information_schema.columns

Examples:

Question:
How many patients are there?

SQL:
SELECT COUNT(*) AS total_patients
FROM patients;

Question:
List all tables

SQL:
SELECT table_name
FROM information_schema.tables
ORDER BY table_name;

Question:
Number of columns in all tables

SQL:
SELECT
    table_name,
    COUNT(*) AS column_count
FROM information_schema.columns
GROUP BY table_name
ORDER BY table_name;
"""

    def is_safe_query(self, query):

        query_lower = query.lower()

        blocked = [
            "drop",
            "delete",
            "update",
            "insert",
            "alter",
            "truncate"
        ]

        for keyword in blocked:

            if keyword in query_lower:
                return False

        return True

    def ask(self, question):

        prompt = f"""
{self.get_schema_prompt()}

Question:
{question}
"""

        sql_query = self.gemini.generate(
            prompt
        )

        sql_query = (
            sql_query
            .replace("```sql", "")
            .replace("```", "")
            .strip()
        )

        if not self.is_safe_query(
            sql_query
        ):
            return "Unsafe query blocked."

        result = self.db.query(
            sql_query
        )

        explanation_prompt = f"""
Question:
{question}

Result:
{result.head(20).to_string()}

Explain this result in simple English.
"""

        explanation = self.gemini.generate(
            explanation_prompt
        )

        return {
            "sql": sql_query,
            "result": result,
            "explanation": explanation
        }