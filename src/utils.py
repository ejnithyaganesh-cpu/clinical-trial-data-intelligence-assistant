def profile_dataset(df, name):

    print(f"\n{name}")

    print("Shape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())


def remove_null_trial_ids(df):

    cleaned_df = df.dropna(
        subset=["trial_id"]
    )

    return cleaned_df


def remove_duplicate_patients(df):

    cleaned_df = df.drop_duplicates(
        subset=["patient_id"]
    )

    return cleaned_df


def remove_invalid_trial_ids(df, trials_df):

    valid_trial_ids = trials_df["trial_id"]

    cleaned_df = df[
        df["trial_id"].isin(valid_trial_ids)
    ]

    return cleaned_df


def clean_patients_data(df, trials_df):

    df = remove_null_trial_ids(df)

    df = remove_invalid_trial_ids(
        df,
        trials_df
    )

    df = remove_duplicate_patients(df)

    return df


def clean_inventory_data(df):

    cleaned_df = df[
        df["quantity_available"] >= 0
    ]

    return cleaned_df