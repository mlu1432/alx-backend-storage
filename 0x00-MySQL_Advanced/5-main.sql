-- Show users and update (or not) email
SELECT * FROM users;

-- Update the valid_email without changing the email
UPDATE users SET valid_email = 1 WHERE email = "bob@dylan.com";

-- Change the email, which should reset valid_email
UPDATE users SET email = "sylvie+new@dylan.com" WHERE email = "sylvie@dylan.com";

-- Update name without changing email, valid_email should remain the same
UPDATE users SET name = "Jannis" WHERE email = "jeanne@dylan.com";

-- Show the updated users
SELECT "--";
SELECT * FROM users;

-- Update email with the same value, valid_email should not change
UPDATE users SET email = "bob@dylan.com" WHERE email = "bob@dylan.com";

-- Show the final result
SELECT "--";
SELECT * FROM users;
