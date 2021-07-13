
--- Normally round function executes for the 4 digits precision but if it does not work for any reason you should use FORMAT(ROUND( , 2) , 'F2') 
--- Here 2 is variable of number that you want to get precision digit. It can be   FORMAT(ROUND( , 3) , 'F3') , FORMAT(ROUND( , 5) , 'F5') and etc.
 
 
 
SELECT FORMAT( ROUND (ABS(MIN(LAT_N)-MAX(LAT_N)) + ABS(MIN(LONG_W)-MAX(LONG_W)) , 4) , 'F4')
FROM STATION ;


