# Clinical Trial Protocol Summary

This project analyzes clinical trial datasets.

The system supports:
- Data loading
- Data quality validation
- SQL KPI generation
- Risk scoring
- LLM-assisted SQL querying

The database backend uses DuckDB.

________________________________________________________________

# Clinical Trial Protocol Summary

## Project Overview

The Clinical Trial AI Assistant is designed to analyze clinical trial datasets, perform data quality validation, generate key performance indicators (KPIs), and support intelligent querying through SQL and AI-based assistants.

---

## Objectives

* Improve clinical trial data quality
* Generate operational and safety KPIs
* Support trial monitoring and reporting
* Enable natural language access to analytics

---

## Data Sources

The system processes the following datasets:

* Patients
* Trials
* Sites
* Visits
* Lab Results
* Adverse Events
* Drug Inventory
* Drug Shipments
* Protocol Deviations
* Reference Codes

---

## Data Processing Workflow

1. Load source datasets
2. Validate data quality
3. Store data in DuckDB
4. Execute KPI SQL queries
5. Generate risk scores
6. Support AI-assisted querying

---

## Key Analytics

### Enrollment Analytics

Tracks patient enrollment across clinical trials.

### Safety Analytics

Tracks adverse events and trial risk.

### Site Performance Analytics

Evaluates participation and operational performance.

### Drug Supply Analytics

Monitors inventory and shipment activity.

---

## Technology Stack

* Python
* Pandas
* DuckDB
* SQL
* LLM SQL Assistant
* Retrieval-Augmented Generation (RAG)

---

## Expected Outcomes

* Reliable clinical trial analytics
* Improved data quality monitoring
* Faster KPI generation
* Natural language interaction with trial data
