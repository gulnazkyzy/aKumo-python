# Task 3: Factorial of a Number (use for loop)
# Input:
# Enter a number: 5

# Output:
# Factorial of 5 is 120

# This first line takes input. Input number can be any number, but for this task input number is 5.
num = int(input("Please enter the number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print(f"The factorial of {num} is {fact}")


# [root@Python Homework]# python task3.py
# Please enter the number: 5
# The factorial of 5 is 120
# [root@Python Homework]#