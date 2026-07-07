import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

from src.database import Database

db = Database()

try:
    db.load_csv_as_table(
        "data/raw/trials.csv",
        "trials"
    )
except:
    pass

try:
    db.load_csv_as_table(
        "data/raw/sites.csv",
        "sites"
    )
except:
    pass

print(
    db.query(
        "SELECT COUNT(*) AS total FROM trials"
    )
)

print(
    db.query(
        "SELECT COUNT(*) AS total FROM sites"
    )
)

db.close()