-- Script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
-- From imported database dump.
SELECT city, AVG(value) as avg_temp FROM temperatures
GROUP BY city ORDER BY avg_temp DESC;
