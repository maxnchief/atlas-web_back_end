-- This SQL script creates a view named 'need_meeting' that selects students
DROP VIEW IF EXISTS need_meeting;
CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE SCORE < 80
AND last_meeting IS NULL
OR last_meeting < DATE_SUB(NOW(), INTERVAL 1 MONTH);