import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

from src.database import Database

db = Database()

db.load_csv_as_table(
    "data/raw/patients.csv",
    "patients"
)

print(
    db.query(
        "SELECT COUNT(*) FROM patients"
    )
)

db.close()