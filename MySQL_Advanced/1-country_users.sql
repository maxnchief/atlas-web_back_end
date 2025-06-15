-- This script creates a table named 'users' with specific constraints on the 'country' column.
CREATE TABLE IF NOT EXISTS users (
    id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country VARCHAR(2) NOT NULL DEFAULT 'US',
    CHECK (country IN ('US', 'CO', 'TN'))
);