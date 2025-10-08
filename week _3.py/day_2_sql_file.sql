1. Write an SQL query to fetch only the first 5 highest salary employees from an employees table.

SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 5;

2. What is the difference between WHERE and LIMIT in SQL?

WHERE
    Used to filter records based on specific conditions.
    It decides which rows should be included in the result set.

LIMIT
    Used to restrict the number of rows returned.
    It decides how many rows should be shown in the result set (after filtering and sorting).

3. Write a query to update the email of a student where id = 10.

    UPDATE students
SET email = 'sriramku007@gmail.com'
WHERE id = 10;

1. Write SQL to create a table students(name, age, marks).

CREATE TABLE students (
    name  VARCHAR(50),
    age   INT,
    marks DECIMAL(5,2)
);

2. Write a query to delete all students who scored below 40 marks.

DELETE FROM students
WHERE marks < 40;

3. Write a query to fetch top 3 students based on marks.

SELECT *
FROM students
ORDER BY marks DESC
LIMIT 3;

