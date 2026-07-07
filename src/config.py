from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw"

PROCESSED_DATA_PATH = PROJECT_ROOT / "data" / "processed"

REJECTED_DATA_PATH = PROJECT_ROOT / "data" / "rejected"

DATABASE_PATH = PROJECT_ROOT / "clinical_trials.duckdb"

SQL_PATH = PROJECT_ROOT / "sql"

OUTPUTS_PATH = PROJECT_ROOT / "outputs"