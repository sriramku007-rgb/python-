#Write a program to split a sentence into words and print each word separately
sentence = input("Enter a sentence: ")
words = sentence.split()
for word in words:
    print(word)