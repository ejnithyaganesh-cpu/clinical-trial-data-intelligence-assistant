from src.database import Database

db = Database()

tables = [
    "patients",
    "trials",
    "sites",
    "visits",
    "lab_results",
    "adverse_events",
    "drug_inventory",
    "drug_shipments",
    "protocol_deviations",
    "reference_codes"
]

for table in tables:

    try:

        db.load_csv_as_table(
            f"data/raw/{table}.csv",
            table
        )

        print("\n")
        print("=" * 50)
        print(table.upper())
        print("=" * 50)

        df = db.query(
            f"SELECT * FROM {table} LIMIT 1"
        )

        print(df.columns.tolist())

    except Exception as e:

        print(table, e)

db.close()