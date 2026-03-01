Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.

Input Format

The STATION table is described as follows:

Station.jpg

where LAT_N is the northern latitude and LONG_W is the western longitude.

https://www.hackerrank.com/challenges/weather-observation-station-11/problem?isFullScreen=true

SELECT DISTINCT CITY FROM STATION WHERE CITY NOT REGEXP "^[a,e,i,o,u].*[a,e,i,o,u]$"