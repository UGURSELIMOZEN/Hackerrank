

----- FIRST APPROACH  -------


SELECT Company.company_code , Company.founder , COUNT(DISTINCT Lead_Manager.lead_manager_code) , COUNT(DISTINCT Senior_Manager.senior_manager_code) ,
COUNT(DISTINCT Manager.manager_code) , COUNT(DISTINCT Employee.employee_code) FROM Company
INNER JOIN Lead_Manager ON Company.company_code = Lead_Manager.company_code
INNER JOIN Senior_Manager ON Senior_Manager.lead_manager_code = Lead_Manager.lead_manager_code
INNER JOIN Manager ON Manager.senior_manager_code = Senior_Manager.senior_manager_code
INNER JOIN Employee ON Employee.manager_code = Manager.manager_code 
GROUP BY Company.company_code , Company.founder 
ORDER BY Company.company_code;





----- SECOND APPROACH  -------- 


SELECT Company.company_code , Company.founder , COUNT(DISTINCT Lead_Manager.lead_manager_code) , COUNT(DISTINCT Senior_Manager.senior_manager_code) ,
COUNT(DISTINCT Manager.manager_code) , COUNT(DISTINCT Employee.employee_code) FROM Company , Lead_Manager , Senior_Manager , Manager , Employee
WHERE  Company.company_code = Lead_Manager.company_code AND Senior_Manager.lead_manager_code = Lead_Manager.lead_manager_code 
AND Manager.senior_manager_code = Senior_Manager.senior_manager_code AND Employee.manager_code = Manager.manager_code 
GROUP BY Company.company_code , Company.founder 
ORDER BY Company.company_code;


