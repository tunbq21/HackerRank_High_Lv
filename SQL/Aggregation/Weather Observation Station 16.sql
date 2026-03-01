https://www.hackerrank.com/challenges/weather-observation-station-16/problem?isFullScreen=true


Query the smallest Northern Latitude (LAT_N) from STATION that is greater than . Round your answer to  decimal places.

Input Format

The STATION table is described as follows:

Station.jpg

where LAT_N is the northern latitude and LONG_W is the western longitude.

SELECT ROUND(MIN(LAT_N), 4) AS lat
FROM STATION
WHERE LAT_N > 38.7880;