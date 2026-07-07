SELECT
    trial_id,
    COUNT(*) AS adverse_event_count
FROM adverse_events
GROUP BY trial_id
ORDER BY adverse_event_count DESC;