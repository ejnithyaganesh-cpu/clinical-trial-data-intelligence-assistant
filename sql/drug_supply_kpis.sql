SELECT
    site_id,
    drug_name,
    quantity_available
FROM drug_inventory
WHERE quantity_available < 100
ORDER BY quantity_available ASC;