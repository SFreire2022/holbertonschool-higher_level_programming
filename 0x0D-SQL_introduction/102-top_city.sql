-- Script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
-- imported in hbtn_0c_0 from this table dump download https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month = 7 OR month = 8
GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
