from src.gemini_client import ask_gemini

schema = """
Tables:

trials
patients
sites
visits
lab_results
adverse_events
drug_inventory
drug_shipments
protocol_deviations
reference_codes
"""

question = """
How many patients are enrolled?
"""

prompt = f"""
You are a SQL expert.

Database Schema:
{schema}

Generate only SQL.

Question:
{question}
"""

response = ask_gemini(prompt)

print(response)