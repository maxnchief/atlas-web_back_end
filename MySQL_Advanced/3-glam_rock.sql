-- This query retrieves the lifespan of glam rock bands by calculating the difference between the year they were formed and the year they split, defaulting to 2020 if no split year is provided.
SELECT band_name, COALESCE(split, 2020) - formed as lifespan FROM metal_bands
WHERE style LIKE '%Glam rock%' ;