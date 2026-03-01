https://www.hackerrank.com/challenges/weather-observation-station-14/problem?isFullScreen=true


Query the greatest value of the Northern Latitudes (LAT_N) from STATION that is less than . Truncate your answer to  decimal places.

Input Format

The STATION table is described as follows:

Station.jpg

where LAT_N is the northern latitude and LONG_W is the western longitude.

SELECT TRUNCATE(MAX(LAT_N), 4) AS lat
FROM STATION
WHERE LAT_N < 137.2345;