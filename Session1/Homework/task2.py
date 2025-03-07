# Task 2: Number Swapper
# Write a Python program that takes two numbers as input from the user and swaps their values.


num1 = input("Enter first number: ")  # This lines takes the input from the user
num2 = input("Enter second number: ")

num1, num2 = num2, num1  # Swap the values

print("after swapping: \nnumber1 is:", num1,"\nnumber2 is:", num2)