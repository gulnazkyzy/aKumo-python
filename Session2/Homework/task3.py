# Task 3: Three-Number Maximum
# Take three integer inputs and print the largest one using only if-elif-else conditions.


# Step1 set 3 variables and ask integer input from user 

num1 = int(input("Please provide the first number: "))
num2 = int(input("Please provide the second number: "))
num3 = int(input("Please provide the third number: "))

if num1 > num2 and num1 > num3:
    print("The largest number is:", num1)
elif num2 > num1 and num2 > num3:
    print("The largest number is:", num2)
else:
    print("The largest number is:", num3)