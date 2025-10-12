1. What is the difference between a class method and an instance method?
instance method
class Student:
    def __init__(self, name):
        self.name = name

    def show_name(self):      
        print("Name:", self.name)
class method
class Student:
    school_name = "ABC School"

    @classmethod
    def show_school(cls):     
        print("School:", cls.school_name)

2. Write a Python function that returns the factorial of a number.

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
num = 5
print("Factorial of", num, "is", factorial(num))

3. How do you append data to an existing file in Python?

with open("example.txt", "a") as file:
    file.write("This is new content.\n")

print("Data appended successfully!")

1. What is the purpose of ON in JOIN operations?

SELECT students.name, classes.class_name
FROM students
JOIN classes
ON students.class_id = classes.class_id;

2. Write a query to get employee name along with their department name using JOIN.

SELECT employees.emp_name, departments.dept_name
FROM employees
JOIN departments
ON employees.dept_id = departments.dept_id;

3. What happens when you JOIN tables without a common key?

SELECT emp_name, dept_name
FROM employees
JOIN departments;
