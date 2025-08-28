#  1 QUESTION Take two integers as input and print their sum, difference, and product.

a=1
b=2
print("Sum:", a + b)
print("Subtraction:", a - b)
print("Product:", a*b)

# 2 QUESTION Input a float and calculate the value after adding 18% tax.

price = int(input("Enter the price before tax: " ))
total_price = price *1.8
print(f"Total price after 18% tax: {total_price:.2f}")

# 3 question Reverse a string taken as input.

text = input("enter a string: ")
reversed_text = text[::-1]
print(f"Reversed string: {reversed_text}")

#4 question Given two boolean inputs, print their AND, OR, and NOT (first value).

a = "true"
b = "false"
and_ok =a and b
or_ok =a or b 
not_ok = not b
print (f"and : {and_ok}")
print (f" or : {or_ok}")
print (f"not: {not_ok}") 

#5 questionIdentify and print the data type of user input after checking if it's int, float, or string.

user_input = input("Enter something:")
try:
    val = int(user_input)
    print("Data type: int")
except ValueError:
    try:
        val = float(user_input)
        print("Data type: float")
    except ValueError:
         print("Data type: string")

        

