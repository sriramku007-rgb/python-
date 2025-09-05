#Write a program to replace all vowels in "hello world" with *.
text= "hollo world"
vowels = "aeiouAEIOU"
for vowel in vowels:
    text = text.replace(vowel, "*")

print(text)