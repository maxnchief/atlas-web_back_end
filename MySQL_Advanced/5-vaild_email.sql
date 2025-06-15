-- This script creates a trigger that sets the valid_email field to 0
DELIMITER $$

CREATE TRIGGER new_email BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email != NEW.email THEN
	SET NEW.valid_email = 0;
    END IF;
END$$

DELIMITER ;