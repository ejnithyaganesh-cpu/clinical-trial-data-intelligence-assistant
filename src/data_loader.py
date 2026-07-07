import pandas as pd
from pathlib import Path

class DataLoader:

    def __init__(self):

        project_root = Path(__file__).resolve().parent.parent

        self.raw_path = project_root / "data" / "raw"

    def load_csv(self, filename):

        file_path = self.raw_path / filename

        return pd.read_csv(file_path)

    def load_trials(self):
        return self.load_csv("trials.csv")

    def load_patients(self):
        return self.load_csv("patients.csv")

    def load_sites(self):
        return self.load_csv("sites.csv")

    def load_visits(self):
        return self.load_csv("visits.csv")

    def load_adverse_events(self):
        return self.load_csv("adverse_events.csv")

    def load_inventory(self):
        return self.load_csv("drug_inventory.csv")

    def load_lab_results(self):
        return self.load_csv("lab_results.csv")

    def load_protocol_deviations(self):
        return self.load_csv("protocol_deviations.csv")

    def load_drug_shipments(self):
        return self.load_csv("drug_shipments.csv")

    def load_reference_codes(self):
        return self.load_csv("reference_codes.csv")