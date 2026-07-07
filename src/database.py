import duckdb
from pathlib import Path


class Database:

    def __init__(self):

        self.db_path = Path("clinical_trials.duckdb")

        self.conn = duckdb.connect(
            str(self.db_path)
        )

    def execute(self, query):

        self.conn.execute(query)

    def query(self, query):

        return self.conn.execute(
            query
        ).fetchdf()

    def load_csv_as_table(
        self,
        csv_path,
        table_name
    ):

        query = f"""
        CREATE OR REPLACE TABLE {table_name}
        AS
        SELECT *
        FROM read_csv_auto('{csv_path}')
        """

        self.conn.execute(query)

    def close(self):

        self.conn.close()