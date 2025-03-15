# Task 1: Number Comparison
# Write a program that takes two integer inputs and prints:
# "Both numbers are equal" if they are the same.
# "The first number is greater" if the first number is larger.
# "The second number is greater" if the second number is larger.

# Step1 set variables and get input from user

num1 = int(input("Please provide the first number: "))
num2 = int(input("Please provide the second number: "))

if num1 == num2:
    print("The numbers are equal")
elif num1 > num2:
    print("The first entered number is greater")
else:
    print("The second entered number is greater")