https://www.hackerrank.com/challenges/weather-observation-station-19/problem?isFullScreen=true


Consider  and  to be two points on a 2D plane where  are the respective minimum and maximum values of Northern Latitude (LAT_N) and  are the respective minimum and maximum values of Western Longitude (LONG_W) in STATION.

Query the Euclidean Distance between points  and  and format your answer to display  decimal digits.

Input Format

The STATION table is described as follows:

Station.jpg

where LAT_N is the northern latitude and LONG_W is the western longitude.

SQRT is the square root function and POWER is the exponentiation function.
POWER(X, Y) returns the value of X raised to the power of Y.



SELECT ROUND(SQRT(POWER((SELECT MAX(LAT_N) FROM STATION) - (SELECT MIN(LAT_N) FROM STATION), 2) + POWER((SELECT MAX(LONG_W) FROM STATION) - (SELECT MIN(LONG_W) FROM STATION), 2)), 4) AS distance;