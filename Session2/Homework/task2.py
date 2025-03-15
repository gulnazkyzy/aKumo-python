# Task 2: Character Type Identifier
# Ask the user to input a single character. Determine and print:
# "It's a digit" if the character is a number (0-9).
# "It's a letter" if the character is a letter (a-z, A-Z).
# "It's a special character" otherwise.

# Step1 get a single character input from user

char = input("Please enter a single character: ")

if char.isnumeric():
    print("It's a digit")
elif char.isalpha():
     print("It's a letter")
else:
     print("It is a special character")