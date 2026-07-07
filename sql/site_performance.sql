SELECT
    site_id,
    COUNT(*) AS patient_count
FROM patients
GROUP BY site_id
ORDER BY patient_count DESC;