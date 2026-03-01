Query the Western Longitude (LONG_W) for the largest Northern Latitude (LAT_N) in STATION that is less than . Round your answer to  decimal places.

Input Format

The STATION table is described as follows:

Station.jpg

where LAT_N is the northern latitude and LONG_W is the western longitude.

Language
MySQL
More
1
Line: 1 Col: 1

Test against custom input
BlogScoring


https://www.hackerrank.com/challenges/weather-observation-station-15/problem?isFullScreen=true


SELECT ROUND(LONG_W, 4) AS lon
FROM STATION
WHERE LAT_N = (SELECT MAX(LAT_N) FROM STATION WHERE LAT_N < 137.2345);