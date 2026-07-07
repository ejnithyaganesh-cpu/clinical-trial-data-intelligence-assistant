from pathlib import Path

from src.database import Database


class SQLQueries:

    def __init__(self):
        self.db = Database()
        self.sql_folder = Path("sql")

    def run_query_file(self, file_name):

        file_path = self.sql_folder / file_name

        if not file_path.exists():
            raise FileNotFoundError(
                f"SQL file not found: {file_path}"
            )

        query = file_path.read_text()

        return self.db.query(query)

    def enrollment_kpis(self):
        return self.run_query_file(
            "enrollment_kpis.sql"
        )

    def adverse_event_kpis(self):
        return self.run_query_file(
            "adverse_events_kpis.sql"
        )

    def site_performance(self):
        return self.run_query_file(
            "site_performance.sql"
        )

    def drug_supply_kpis(self):
        return self.run_query_file(
            "drug_supply_kpis.sql"
        )

    def trial_risk_score(self):
        return self.run_query_file(
            "trial_risk_score.sql"
        )

    def close(self):
        self.db.close()