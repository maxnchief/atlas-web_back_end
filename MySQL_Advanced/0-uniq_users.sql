-- This SQL script creates a table named 'users' with the following columns:
CREATE TABLE IF NOT EXISTS users (
    id INTEGER NOT NULL PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
