https://www.hackerrank.com/challenges/weather-observation-station-13/problem?isFullScreen=true


Query the sum of Northern Latitudes (LAT_N) from STATION having values greater than  and less than . Truncate your answer to  decimal places.

Input Format

The STATION table is described as follows:

Station.jpg

where LAT_N is the northern latitude and LONG_W is the western longitude.


TRUNCATE is a function that truncates a number to a specified number of decimal places. It takes two arguments: the number to be truncated and the number of decimal places to keep. For example, TRUNCATE(3.14159, 2) would return 3.14. # ko làm tròn chỉ giới hạn phần thập phân cần lấy.

SELECT TRUNCATE(SUM(LAT_N), 4) AS lat
FROM STATION
WHERE LAT_N > 38.7880 AND LAT_N < 137.2345;  