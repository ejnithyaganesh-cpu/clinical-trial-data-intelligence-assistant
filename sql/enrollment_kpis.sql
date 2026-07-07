SELECT
    trial_id,
    COUNT(*) AS enrolled_patients
FROM patients
WHERE enrollment_status = 'Enrolled'
GROUP BY trial_id
ORDER BY enrolled_patients DESC;