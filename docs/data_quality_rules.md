# Data Quality Rules

1. Patient IDs must be unique.
2. Trial IDs must be valid.
3. Site IDs must exist in the site master table.
4. Required fields cannot be null.
5. Duplicate records are not allowed.

____________________________________________________________

# Data Quality Rules

## Overview

The Clinical Trial AI Assistant performs data quality validation before analytics and KPI generation.

---

## Patient Data Rules

### Patient ID Validation

* Patient IDs must be unique.
* Patient IDs cannot be null.

### Demographic Validation

* Age must be greater than 0.
* Gender must not be empty.

---

## Trial Data Rules

### Trial ID Validation

* Trial IDs must be unique.
* Trial IDs cannot be null.

### Trial Status Validation

* Trial status must contain valid values.

---

## Site Data Rules

### Site ID Validation

* Site IDs must be unique.
* Site IDs cannot be null.

### Site Reference Validation

* Patient site IDs must exist in the Sites dataset.

---

## Missing Value Checks

The system identifies:

* Null values
* Blank values
* Missing records

---

## Duplicate Checks

The system identifies:

* Duplicate rows
* Duplicate identifiers
* Repeated records

---

## Validation Outcome

Each dataset is classified as:

* PASS
* WARNING
* FAIL

based on detected data quality issues.
