-- This script creates a table `users` with unique constraints on the `email` column
-- The `id` column is an auto-incrementing primary key
-- The `email` column must be unique and cannot be null

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    PRIMARY KEY (id)
);
