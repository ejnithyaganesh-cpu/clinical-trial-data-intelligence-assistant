import pandas as pd


class RiskScoring:

    def calculate_trial_risk(self, adverse_events_df):

        risk_df = adverse_events_df.copy()

        risk_df["risk_score"] = risk_df[
            "adverse_event_count"
        ].apply(
            self.assign_risk_level
        )

        return risk_df

    def assign_risk_level(self, count):

        if count >= 100:
            return "HIGH"

        elif count >= 80:
            return "MEDIUM"

        else:
            return "LOW"