-- This script creates the table 'id_not_null'

-- create the table if it does not exist
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT NOT NULL DEFAULT 1,
	name VARCHAR(256)
);
