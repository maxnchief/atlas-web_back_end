-- Description: This script creates a function to safely divide two integers, returning 0 if the divisor is zero.
DELIMITER //

DROP FUNCTION IF EXISTS SafeDiv;
CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS FLOAT DETERMINISTIC BEGIN IF b = 0 THEN RETURN 0;
END IF;
RETURN a / b;
END;
DELIMITER; //