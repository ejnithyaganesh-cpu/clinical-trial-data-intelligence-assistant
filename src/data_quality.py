import pandas as pd


class DataQuality:

    def check_null_patient_id(self, df):

        invalid_records = df[df["patient_id"].isnull()]

        return invalid_records


    def check_null_trial_id(self, df):

        invalid_records = df[df["trial_id"].isnull()]

        return invalid_records


    def check_valid_trial_id(self, df, trials_df):

        valid_trial_ids = trials_df["trial_id"]

        invalid_records = df[
            ~df["trial_id"].isin(valid_trial_ids)
        ]

        return invalid_records


    def check_valid_site_id(self, df, sites_df):

        valid_site_ids = sites_df["site_id"]

        invalid_records = df[
            ~df["site_id"].isin(valid_site_ids)
        ]

        return invalid_records


    def check_duplicate_patient_id(self, df):

        duplicate_records = df[
            df.duplicated(subset=["patient_id"])
        ]

        return duplicate_records


    def check_missing_trial_status(self, trials_df):

        invalid_records = trials_df[
            trials_df["trial_status"].isnull()
        ]

        return invalid_records


    def check_negative_inventory(self, inventory_df):

        invalid_records = inventory_df[
            inventory_df["quantity_available"] < 0
        ]

        return invalid_records


    # VISITS

    def check_null_visit_id(self, visits_df):

        invalid_records = visits_df[
            visits_df["visit_id"].isnull()
        ]

        return invalid_records


    def check_valid_visit_patient_id(
        self,
        visits_df,
        patients_df
    ):

        valid_patient_ids = patients_df["patient_id"]

        invalid_records = visits_df[
            ~visits_df["patient_id"].isin(
                valid_patient_ids
            )
        ]

        return invalid_records


    # LAB RESULTS

    def check_valid_visit_id(
        self,
        lab_results_df,
        visits_df
    ):

        valid_visit_ids = visits_df["visit_id"]

        invalid_records = lab_results_df[
            ~lab_results_df["visit_id"].isin(
                valid_visit_ids
            )
        ]

        return invalid_records


    def check_missing_result_value(
        self,
        lab_results_df
    ):

        invalid_records = lab_results_df[
            lab_results_df["result_value"].isnull()
        ]

        return invalid_records


    # ADVERSE EVENTS

    def check_null_ae_id(
        self,
        adverse_events_df
    ):

        invalid_records = adverse_events_df[
            adverse_events_df["ae_id"].isnull()
        ]

        return invalid_records


    # DRUG SHIPMENTS

    def check_negative_quantity_shipped(
        self,
        shipments_df
    ):

        invalid_records = shipments_df[
            shipments_df["quantity_shipped"] < 0
        ]

        return invalid_records