-- 5-valid_email.sql
-- This script creates a trigger that resets the valid_email attribute
-- to 0 (false) whenever the email field is updated to a new value.

DELIMITER $$

CREATE TRIGGER reset_valid_email_before_update
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END$$

DELIMITER ;
