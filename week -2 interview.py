# Write a Python program to count the frequency of each character in a string.

def char_frequency(string):
    freq = {}  
    for char in string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq
text = input("Enter a string: ")
result = char_frequency(text)

print("\nCharacter Frequencies:")
for char, count in result.items():
    print(f"'{char}': {count}")

#Write a Python function to remove duplicates from a list without using set()

def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:   
            unique_list.append(item)
    return unique_list
numbers = [1, 2, 3, 2, 4, 1, 5, 3]
print("Original list:", numbers)
print("List without duplicates:", remove_duplicates(numbers))

#Write a program to find the second largest number in a list without sorting.

def second_largest(lst):
    if len(lst) < 2:
        return None  
    
    largest = second = float('-inf')
    
    for num in lst:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    
    return second if second != float('-inf') else None
numbers = [10, 20, 4, 45, 99, 99, 45]
print("List:", numbers)
print("Second largest number:", second_largest(numbers))

#Write a function that returns all prime numbers within a given range.

def primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1: 
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes
print("Prime numbers between 10 and 50:", primes_in_range(10, 50))

#Write a recursive function to calculate the sum of digits of a number.

def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_of_digits(n // 10)


num = 9875
print(f"Sum of digits of {num} is:", sum_of_digits(num))

#Create a class Temperature that takes Celsius as input and calculates Fahrenheit using @property.

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius  

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._celsius = value

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

t = Temperature(25)
print("Celsius:", t.celsius)         
print("Fahrenheit:", t.fahrenheit)   

t.celsius = 0
print("Celsius:", t.celsius)         
print("Fahrenheit:", t.fahrenheit)   

#Write a loop that keeps asking the user for a valid number until correct input is entered.

while True:
    try:
        num = int(input("Enter a valid number: "))
        print(f"You entered: {num}")
        break 
    except ValueError:
        print("Invalid input! Please enter a number.")