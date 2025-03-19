# Agenda 

# - for else and while else 
# - Functions
# - Recursive functions
# - Exceptions / Error Handling
# - Exception Classes 

# for char in "Hello":
#     print(char)
#     if  char == 'l':


# numberChecker ([1,2,3,4], 3)
# --> True | False

# required argument comes first in the function

# def numberChecker(number=2, lst=[1, 2, 3, 4]):
#     if number in lst:
#         return True
#     else:
#         return False

# print(numberChecker(5, [5, 6, 7, 8, 9, 10]))


# Recursive function 

# def test():
# test()

# program needs to print from 1 - 10
# n = 1
# while <condition>
#     if n == 10
#        break
#     else:
#        print(n)
#        n = n + 1 ---> ensures 


# What is the Factorial ----> 6! ---> 6 * 5 * 4 * 3 * 2 * 1

def factorial(n):
    if n == 1:  # breaking point
        return 1
    return n * factorial(n - 1)  # call yourself once again

# # factorial of 5
# # n = 5

# # 5 * 4 * 3 * 2 * 1

# # factorial(4) == 4 * 3 * 2 * 1
# # n = 4
# # 4 * factorial(3)

# # factorial(3)
# # n = 3
# # 3 * 2 * 1


# # factorial(2)
# # n = 2
# # 2 * 1

# # factorial(1) == 1
# # return 1

# print(factorial(5))  # 5 * 4 * 3 * 2 * 1 == 120




