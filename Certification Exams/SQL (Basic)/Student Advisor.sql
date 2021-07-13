


SET NOCOUNT ON;


SELECT roll_number , name FROM student_information , faculty_information
WHERE (advisor = employee_id AND gender = 'M' AND salary > 15000) OR (advisor = employee_id AND gender = 'F' AND salary > 20000)  ;  

go



