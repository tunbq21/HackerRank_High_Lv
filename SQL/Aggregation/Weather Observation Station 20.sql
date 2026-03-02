https://www.hackerrank.com/challenges/weather-observation-station-20/problem?isFullScreen=true



A median is defined as a number separating the higher half of a data set from the lower half. Query the median of the Northern Latitudes (LAT_N) from STATION and round your answer to  decimal places.

Input Format

The STATION table is described as follows:

Station.jpg

where LAT_N is the northern latitude and LONG_W is the western longitude.


SET @row_index := -1;

SELECT ROUND(AVG(sub.LAT_N), 4)
FROM (
    SELECT @row_index := @row_index + 1 AS row_id, LAT_N
    FROM STATION
    ORDER BY LAT_N
) AS sub
WHERE sub.row_id IN (FLOOR(@row_index / 2), CEIL(@row_index / 2));   