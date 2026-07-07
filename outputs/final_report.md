# Clinical Trial Data Intelligence Assistant

## Project Summary

This project analyzes clinical trial datasets, performs data quality validation, cleans invalid records, stores processed data, generates KPIs using SQL, and calculates trial risk scores.

---

# Data Overview

Datasets Used:

- patients.csv
- trials.csv
- sites.csv
- visits.csv
- lab_results.csv
- adverse_events.csv
- drug_inventory.csv
- drug_shipments.csv
- protocol_deviations.csv
- reference_codes.csv

---

# Data Quality Validation

The following validation rules were implemented:

### Patients

- Null Patient ID Check
- Null Trial ID Check
- Valid Trial ID Check
- Valid Site ID Check
- Duplicate Patient ID Check

### Trials

- Missing Trial Status Check

### Visits

- Null Visit ID Check
- Invalid Patient ID Check

### Lab Results

- Invalid Visit ID Check
- Missing Result Value Check

### Adverse Events

- Null Adverse Event ID Check

### Drug Inventory

- Negative Inventory Check

### Drug Shipments

- Negative Shipment Quantity Check

---

# Data Cleaning Summary

Before Cleaning:

- Patients Rows: 318
- Null Trial IDs: 1
- Invalid Trial IDs: 1
- Duplicate Patient IDs: 1
- Negative Inventory Records: 1

After Cleaning:

- Patients Rows: 316
- Null Trial IDs: 0
- Invalid Trial IDs: 0
- Duplicate Patient IDs: 0
- Negative Inventory Records: 0

Records Removed:

- Patient Records Removed: 2
- Inventory Records Removed: 1

---

# SQL KPIs

## Enrollment KPI

Measures enrolled patients per trial.

Query:

- enrollment_kpis.sql

---

## Adverse Events KPI

Measures adverse event count per trial.

Query:

- adverse_events_kpis.sql

---

## Site Performance KPI

Measures patient enrollment per site.

Query:

- site_performance.sql

---

## Drug Supply KPI

Identifies low inventory sites.

Query:

- drug_supply_kpis.sql

---

## Trial Risk Score KPI

Measures trial risk using adverse event counts.

Query:

- trial_risk_score.sql

---

# Risk Scoring

Risk Levels:

- HIGH → Adverse Events >= 100
- MEDIUM → Adverse Events >= 80
- LOW → Adverse Events < 80

Example:

| Trial ID | Risk Level |
|-----------|------------|
| CT-NEUR-004 | HIGH |
| CT-CARD-002 | HIGH |
| CT-DIAB-003 | MEDIUM |
| CT-ONC-001 | MEDIUM |

---

# Technology Stack

- Python
- Pandas
- DuckDB
- SQL

---

# Project Status

Completed:

- Data Loading
- Data Quality Validation
- Data Cleaning
- Processed Data Generation
- Rejected Data Tracking
- SQL KPI Generation
- Risk Scoring

Next Phase:

- LLM SQL Assistant
- RAG Assistant