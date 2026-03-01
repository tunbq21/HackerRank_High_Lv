https://www.hackerrank.com/challenges/weather-observation-station-18/problem?isFullScreen=true

Consider  and  to be two points on a 2D plane.

 happens to equal the minimum value in Northern Latitude (LAT_N in STATION).
 happens to equal the minimum value in Western Longitude (LONG_W in STATION).
 happens to equal the maximum value in Northern Latitude (LAT_N in STATION).
 happens to equal the maximum value in Western Longitude (LONG_W in STATION).
Query the Manhattan Distance between points  and  and round it to a scale of  decimal places.

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



SELECT ROUND(ABS((SELECT MIN(LAT_N) FROM STATION) - (SELECT MAX(LAT_N) FROM STATION)) + ABS((SELECT MIN(LONG_W) FROM STATION) - (SELECT MAX(LONG_W) FROM STATION)), 4) AS distance;