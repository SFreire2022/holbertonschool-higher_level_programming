-- Script that displays the max temperature of each state (ordered by State name)
-- imported to hbtn_0c_0 from this table dump download https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
