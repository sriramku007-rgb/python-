1. What is the difference between INNER JOIN and LEFT JOIN?

INNER JOIN:
SELECT students.name, marks.marks
FROM students
INNER JOIN marks ON students.id = marks.student_id;
    
LEFT JOIN:
SELECT students.name, marks.marks
FROM students
LEFT JOIN marks ON students.id = marks.student_id;

2. Write a query to count how many students are in each class using GROUP BY.

SELECT class, COUNT(*) AS total_students
FROM students
GROUP BY class;

3. What is the purpose of the HAVING clause when WHERE already exists?

SELECT class, AVG(marks) AS avg_marks
FROM students
WHERE marks > 60
GROUP BY class;

1. Write a query to get the highest marks subject-wise.

SELECT subject, MAX(marks) AS highest_marks
FROM students
GROUP BY subject;

2. Write SQL to get the total number of students per department.

SELECT department, COUNT(*) AS total_students
FROM students
GROUP BY department;

3. Write a query to calculate the average marks of top 5 students.

SELECT AVG(marks) AS average_top_5
FROM (
    SELECT marks
    FROM students
    ORDER BY marks DESC
    LIMIT 5
) AS top_students;
