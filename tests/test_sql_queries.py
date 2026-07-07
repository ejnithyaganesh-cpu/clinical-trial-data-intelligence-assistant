import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

from src.database import Database
from src.sql_queries import SQLQueries


db = Database()

db.load_csv_as_table(
    "data/raw/adverse_events.csv",
    "adverse_events"
)

queries = SQLQueries()

print("\nTRIAL RISK SCORE")
print(
    queries.trial_risk_score()
)

queries.close()
db.close()