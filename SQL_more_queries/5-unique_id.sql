-- setting a Unique value
CREATE TABLE IF NOT EXISTS unique_id(
    id INT NOT NULL DEFAULT 1 Unique,
    name VARCHAR(256)
)