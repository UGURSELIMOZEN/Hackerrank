

SELECT MAX(salary*months) AS earnings, COUNT(salary*months) FROM Employee 
WHERE (salary*months) IN (SELECT MAX(salary*months) FROM Employee);

