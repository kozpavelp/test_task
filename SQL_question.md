# Варианты решения

1.
UPDATE full_names
SET status = short_names.status
FROM short_names
WHERE full_names.name || '.mp3' LIKE short_names.name || '%';

2.
UPDATE full_names
SET status = (
    SELECT status
    FROM short_names
    WHERE short_names.name || '.mp3' = full_names.name
);