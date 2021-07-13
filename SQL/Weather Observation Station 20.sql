--- Normally round function executes for the 4 digits precision but if it does not work for any reason you should use FORMAT(ROUND( , 2) , 'F2') 
--- Here 2 is variable of number that you want to get precision digit. It can be   FORMAT(ROUND( , 3) , 'F3') , FORMAT(ROUND( , 5) , 'F5') and etc.



SELECT FORMAT(ROUND(S.LAT_N,4) ,'F4') FROM STATION AS S 
WHERE (SELECT COUNT(LAT_N) FROM STATION WHERE LAT_N < S.LAT_N ) = (SELECT COUNT(LAT_N) FROM STATION WHERE LAT_N > S.LAT_N);


