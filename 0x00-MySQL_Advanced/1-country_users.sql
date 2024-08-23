-- This script creates a table `users` with a country enumeration
-- The `id` column is an auto-incrementing primary key
-- The `email` column is unique and cannot be null
-- The `name` column is a string with a maximum length of 255 characters
-- The `country` column is an ENUM with values 'US', 'CO', 'TN', and defaults to 'US'

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US',
    PRIMARY KEY (id)
);
