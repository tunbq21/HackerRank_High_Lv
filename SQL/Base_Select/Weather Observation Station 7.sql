Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.

Input Format

The STATION table is described as follows:

Station.jpg

https://www.hackerrank.com/challenges/weather-observation-station-7/problem?isFullScreen=true



where LAT_N is the northern latitude and LONG_W is the western longitude.

SELECT DISTINCT CITY 
FROM STATION 
WHERE CITY REGEXP '^[aeiou].*[aeiou]$';

Select DISTINCT CITY from STATION where CITY REGEXP '^[a,e,i,o,u].*[a,e,i,o,u]$'