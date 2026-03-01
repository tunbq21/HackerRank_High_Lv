

Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.

Input Format

The STATION table is described as follows:

Station.jpg


https://www.hackerrank.com/challenges/weather-observation-station-6/problem?isFullScreen=true


SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '^[aeiouAEIOU]'

SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP "^[a, e, i, o, u]"