-- list the scores and the number of times they occur
SELECT score, count(score) AS number
FROM second_table
GROUP BY score
ORDER BY number
DESC;
