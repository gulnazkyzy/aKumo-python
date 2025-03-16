#Task 1: Reverse a List
# Write a program that reverses a list using a for loop.
# Example:
# # Input:
# Enter numbers separated by space: 1 2 3 4 5
# # Output:
# Reversed List: [5, 4, 3, 2, 1]

# Take input numbers
num = input("Please input your numbers: ").split()
reversed_num = []
for i in range(len(num)):
    reversed_num.append(num[-(i+1)])
print("Reversed List: ", reversed_num)