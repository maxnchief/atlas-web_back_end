-- This SQL script creates an index on the `names` table
CREATE INDEX idx_name_first_score
ON names(name(1), score);