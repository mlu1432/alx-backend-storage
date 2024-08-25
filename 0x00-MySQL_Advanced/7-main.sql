-- Show users and their corrections before computing average score
SELECT * FROM users;
SELECT * FROM corrections;

SELECT "--";

-- Compute the average score for Jeanne
CALL ComputeAverageScoreForUser((SELECT id FROM users WHERE name = "Jeanne"));

SELECT "--";

-- Show users after computing average score
SELECT * FROM users;
