# Data Dictionary

## trials.csv

| Column            | Description             |
| ----------------- | ----------------------- |
| trial_id          | Unique trial identifier |
| phase             | Clinical trial phase    |
| indication        | Disease area            |
| sponsor           | Trial sponsor           |
| target_enrollment | Planned enrollment      |

## patients.csv

| Column            | Description               |
| ----------------- | ------------------------- |
| patient_id        | Unique patient identifier |
| trial_id          | Associated trial          |
| site_id           | Associated site           |
| enrollment_status | Enrollment status         |
| treatment_arm     | Treatment assignment      |

## adverse_events.csv

| Column           | Description             |
| ---------------- | ----------------------- |
| adverse_event_id | Event identifier        |
| patient_id       | Associated patient      |
| trial_id         | Associated trial        |
| serious_flag     | Indicates serious event |

## sites.csv

| Column            | Description            |
| ----------------- | ---------------------- |
| site_id           | Site identifier        |
| investigator      | Principal investigator |
| country           | Site country           |
| activation_status | Site status            |
