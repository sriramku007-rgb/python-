#Reverse the number 12345 using a while loop
num = 12345
reversed_num = 0

while num > 0:
    digit = num % 10             
    reversed_num = reversed_num * 10 + digit 
    num = num // 10            

print("Reversed number is:", reversed_num)