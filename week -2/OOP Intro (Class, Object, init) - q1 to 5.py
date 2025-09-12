#Create a class Car with attributes brand and year. Create an object and print its details.

class Car:
    def __init__(self,brand, year):
        self.brand = brand
        self.year = year
    def display_details(self):
        print(f"brand: {self.brand}") 
        print(f"year: {self.year}")    

my_car = Car("Toyota", 2020)
my_car.display_details()

#Create a class Student with attributes name and age. Initialize them using _init_ and create 2 student objects.

class Student:
    def __init__(self,name,age):
        self.name  = name
        self.age = age

student1 = Student("sri", 20)
student2 = Student("ram", 22)
print("Student 1:", student1.name, "-", student1.age)
print("Student 2:", student2.name, "-", student2.age)

#Create a class Circle with an attribute radius. Add a method area() that returns the area of the circle.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
circle1 = Circle(5)
print("Area of the circle:", circle1.area())

#Create a class Book with attributes title and author. Create 3 book objects and print their details.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
book1 = Book("To Kill a Mockingbird", "Harper Lee")
book2 = Book("1984", "George Orwell")
book3 = Book("Pride and Prejudice", "Jane Austen")
print("Book 1:", book1.title, "by", book1.author)
print("Book 2:", book2.title, "by", book2.author)
print("Book 3:", book3.title, "by", book3.author)

#Create a class BankAccount with attributes owner and balance. Add methods:

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds.")
account = BankAccount("Sriramkumar", 100)
account.deposit(50)    
account.withdraw(30)    
account.withdraw(150)   

