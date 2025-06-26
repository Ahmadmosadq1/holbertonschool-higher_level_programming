-- Selecting all records
SELECT score, name FROM second_table
WHERE name is NOT NULL AND name != ''
ORDER BY score DESC;
