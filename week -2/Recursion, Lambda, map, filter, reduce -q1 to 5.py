# #Write a recursive function factorial(n) that returns the factorial of n.
def factorial(n):
    if n== 0 or n== 1 :
        return 1
    else:
        return n * factorial (n - 1)
print(factorial(5))

# #Write a recursive function fibonacci(n) that returns the nth Fibonacci number.

def fibonacci(n):
    if n== 0:
        return 0
    elif n ==1:
        return 1 
    else: 
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(6))

#Use map() with a lambda to square all numbers in a list [1, 2, 3, 4, 5].

numbers = [1,2,3,4,5]
squared = list(map(lambda x:x**2, numbers))
print(squared)
 
#Use filter() with a lambda to get all even numbers from a list [10, 15, 20, 25, 30].

numbers = [10,15,20,25,30]
evens = list(filter(lambda x:x % 2 == 0 ,numbers))
print(evens)

#Use reduce() with a lambda to compute the product of numbers in a list [1, 2, 3, 4, 5].

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)