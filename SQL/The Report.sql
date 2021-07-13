


SELECT
  CASE
    WHEN GRADES.grade < 8 THEN NULL
    ELSE STUDENTS.name
  END,
  GRADES.grade,
  STUDENTS.marks
FROM students 
INNER JOIN GRADES ON STUDENTS.marks >= GRADES.min_mark AND STUDENTS.marks <= GRADES.max_mark
ORDER BY GRADES.grade DESC, STUDENTS.name ;



