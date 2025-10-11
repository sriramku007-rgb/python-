1. Explain the difference between UNIQUE and PRIMARY KEY constraints.

CREATE TABLE students (
    student_id INT PRIMARY KEY,       
   email VARCHAR(100) UNIQUE,        
    phone VARCHAR(15) UNIQUE NOT NULL 
    );

2. Write a query to select students who scored above the average marks of all students (using subquery).

SELECT name, marks
FROM students
WHERE marks > (SELECT AVG(marks) FROM students);

3. What is a foreign key and why is it important?

CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    dept_id INT,
    marks INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

1. Write pseudocode for inserting a student record using Python and SQLite.


import sqlite3                     

conn = sqlite3.connect('school.db')
cursor = conn.cursor()               # Step 3: Create cursor
sql = "INSERT INTO students (name, age, marks) VALUES (?, ?, ?)"
data = ("John", 18, 85)
cursor.execute(sql, data)
conn.commit()

print("Record inserted successfully!")  
conn.close()


2. What is the purpose of parameterized queries in Python SQL integration?

cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("John", 18))

