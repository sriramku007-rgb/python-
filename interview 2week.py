#Write a function is_even(n) that returns True if a number is even, else False.
def is_even(n)
return n % 2 == 0
print (is_even(4))
print (is_even(7))

# Write a recursive function to calculate the factorial of a number.

def factorial (a)
if n == 0 or n == 1:
    return 1 
    else:
        return n * factorial (n - 1)
 print (factorial(5))

#Use lambda + filter to extract only even numbers from a list nums = [1,2,3,4,5,6].

nums = [1,2,3,4,5,6]
even_nums = list (filter(loambda x: x % 2== 0,nums))
print (even_nums) 
 
#Create a base class Animal with a method sound(). Create subclasses Dog and Cat that override it.

clss animal: 
      def sound (self)
      return "some generic animal sound"
       
class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

a = Animal()
d = Dog()
c = Cat()

print(a.sound())  
print(d.sound())  
print(c.sound())  

#Write Python code that opens data.txt, reads content, and handles file not found.

try:
    with open('data.txt', 'r') as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print("Error: 'data.txt' not found.")