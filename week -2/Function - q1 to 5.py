#Write a function greet(name) that takes a person’s name as a parameter and returns a greeting 
def greet(name):
    return f"Hello, {name}!"
print (greet("sriram"))

#Write a function sum_of_list(numbers) that takes a list of integers and returns the sum.
def sum_of_list(number):
    return sum(number)
print(sum_of_list([11,22,33,44,55,66,77]))

#Write a function find_max(a, b, c) that takes three numbers and returns the largest one.

def find_max(a, b, c):
    return max(a, b, c)
print(find_max(10, 25, 7))

#Write a function factorial(n) that returns the factorial of a number without using recursion.

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
print(factorial(5))  
print(factorial(0))  

#Write a function is_prime(num) that returns True if a number is prime, otherwise False.

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True
print(is_prime(2))   
print(is_prime(17))  
print(is_prime(18))  
print(is_prime(1))   

