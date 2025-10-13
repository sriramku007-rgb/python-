1. Write pseudocode for fetching data from a SQL table and printing it in Python.

import sqlite3
conn = sqlite3.connect("school.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.close()
conn.close()

2. How would you display all student names whose marks are > 80 using Python + SQL?

import sqlite3
conn = sqlite3.connect("school.db")
cursor = conn.cursor()
cursor.execute("SELECT name FROM students WHERE marks > 80")
rows = cursor.fetchall()
for row in rows:
    print("Student Name:", row[0])

cursor.close()
conn.close()

3. In which situation would you use fetchone() vs fetchall()?

cursor.execute("SELECT name FROM students WHERE id = 1")
row = cursor.fetchone()
print(row)

cursor.execute("SELECT name FROM students WHERE marks > 80")
rows = cursor.fetchall()
for row in rows:
    print(row)

1. List the core features required in a Student Management System.

1. Student Information Storage
Create a table to store student details.
Fields: student_id, name, age, gender, class_id, address, contact_no, email.
Use PRIMARY KEY on student_id.

2. Course / Subject Management
Table to store subjects or courses offered.
Fields: subject_id, subject_name, teacher_id, credits.

3. Class / Department Management
Table: class_id, class_name, department_name.

4. Marks / Grades Management
Table to store students’ exam results.
Fields: mark_id, student_id, subject_id, marks, grade.
Use FOREIGN KEY references to students and subjects.

5. Attendance Management
Table: attendance_id, student_id, date, status (‘Present’/‘Absent’).

6. Teacher Information
Table: teacher_id, name, department, email, phone.

7. Fee Management
Table: fee_id, student_id, amount, paid_date, due_date, status.

8. Relationship Management (Foreign Keys)
Use FOREIGN KEY constraints to link:
students.class_id → classes.class_id
marks.student_id → students.student_id
marks.subject_id → subjects.subject_id
subjects.teacher_id → teachers.teacher_id

9. Reports and Queries
Build SQL queries to:
Get total students per class (GROUP BY class_id)
Calculate average marks per subject (AVG(marks))
List top-performing students (ORDER BY marks DESC LIMIT 5)
Find students with pending fees

2. Explain how you would design the database schema for a Library Management System.

CREATE TABLE Category (
    category_id INT PRIMARY KEY,
    category_name VARCHAR(100)
);

CREATE TABLE Books (
    book_id INT PRIMARY KEY,
    title VARCHAR(100),
    author VARCHAR(100),
    publisher VARCHAR(100),
    year_published INT,
    category_id INT,
    total_copies INT,
    available_copies INT,
    FOREIGN KEY (category_id) REFERENCES Category(category_id)
);

CREATE TABLE Members (
    member_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(15),
    address VARCHAR(200),
    join_date DATE
);

CREATE TABLE Staff (
    staff_id INT PRIMARY KEY,
    name VARCHAR(100),
    role VARCHAR(50),
    email VARCHAR(100)
);

CREATE TABLE Borrow (
    issue_id INT PRIMARY KEY,
    book_id INT,
    member_id INT,
    staff_id INT,
    issue_date DATE,
    due_date DATE,
    return_date DATE,
    FOREIGN KEY (book_id) REFERENCES Books(book_id),
    FOREIGN KEY (member_id) REFERENCES Members(member_id),
    FOREIGN KEY (staff_id) REFERENCES Staff(staff_id)
);

3. What are the advantages of integrating SQL with Python compared to using Excel files?

1. Data Storage and Scalability
SQL + Python: Databases can store millions of records efficiently and handle concurrent access.
Excel: Limited to around 1 million rows per sheet and slows down with large datasets.

2. Data Integrity and Relationships
SQL: Supports PRIMARY KEY, FOREIGN KEY, UNIQUE, and CHECK constraints to ensure accurate and related data.
Excel: No built-in mechanism to enforce relationships between data sheets.

3. Querying Power
SQL: Can perform complex operations like JOINs, GROUP BY, HAVING, nested queries, and aggregate functions.
Excel: Relies on formulas and filters; handling relational data is difficult.

4. Automation with Python
Python + SQL: You can automate data tasks like fetching, inserting,
updating, or generating reports using Python scripts.
Excel: Mostly manual operations or limited VBA scripting.

5. Security and Access Control
SQL: Databases have user authentication, roles, and permissions to control access.
Excel: Basic password protection only; easy to modify or copy files.

6. Multi-user Access
SQL: Multiple users can connect and modify data simultaneously without conflict.
Excel: Designed for single-user use; concurrent edits cause file corruption or version issues.

7. Data Analysis and Reporting
Python + SQL: You can query SQL data directly and visualize it using Python libraries like matplotlib, pandas, or seaborn.
Excel: Has built-in charts but is not ideal for dynamic, large-scale analysis.

8. Data Backup and Recovery
SQL: Supports transactions, rollback, and backups for safety.
Excel: No built-in transaction control or automatic recovery.