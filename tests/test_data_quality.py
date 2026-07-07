import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.data_loader import DataLoader
from src.data_quality import DataQuality
from src.utils import (
    clean_patients_data,
    clean_inventory_data
)

loader = DataLoader()
dq = DataQuality()

patients = loader.load_patients()
trials = loader.load_trials()
inventory = loader.load_inventory()

print("=" * 60)
print("DATA CLEANING REPORT")
print("=" * 60)

# -------------------------
# BEFORE CLEANING
# -------------------------

print("\nBEFORE CLEANING")

print("Patients Rows:", len(patients))
print(
    "Null Trial IDs:",
    len(dq.check_null_trial_id(patients))
)
print(
    "Invalid Trial IDs:",
    len(dq.check_valid_trial_id(patients, trials))
)
print(
    "Duplicate Patient IDs:",
    len(dq.check_duplicate_patient_id(patients))
)

print(
    "Negative Inventory Records:",
    len(dq.check_negative_inventory(inventory))
)

# -------------------------
# CLEAN DATA
# -------------------------

patients_cleaned = clean_patients_data(
    patients,
    trials
)

inventory_cleaned = clean_inventory_data(
    inventory
)

# -------------------------
# AFTER CLEANING
# -------------------------

print("\nAFTER CLEANING")

print("Patients Rows:", len(patients_cleaned))
print(
    "Null Trial IDs:",
    len(dq.check_null_trial_id(patients_cleaned))
)
print(
    "Invalid Trial IDs:",
    len(
        dq.check_valid_trial_id(
            patients_cleaned,
            trials
        )
    )
)
print(
    "Duplicate Patient IDs:",
    len(
        dq.check_duplicate_patient_id(
            patients_cleaned
        )
    )
)

print(
    "Negative Inventory Records:",
    len(
        dq.check_negative_inventory(
            inventory_cleaned
        )
    )
)

print("\nSUMMARY")

print(
    "Patient Rows Removed:",
    len(patients) - len(patients_cleaned)
)

print(
    "Inventory Rows Removed:",
    len(inventory) - len(inventory_cleaned)
)

print("\n" + "=" * 60)
print("TEST COMPLETED")
print("=" * 60)