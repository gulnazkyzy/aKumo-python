# Numeric Data Type

# - Binary - 0b  -----> 01010101
# - Octal - 0o -------> 0-7
# - Hexidecimal - 0x --> 16 --> 0-9 abcdf


# print 21
# print(0b010101)

# # convert 21 to binary
# print(bin(21))

# print(oct(21))
# print(hex(21))

# String Concatination 

# word1 = "Hello"
# word2 = "World"
# combined = word1 + word2
# print(combined) 

### Boolean
# Boolean data types True or False
# Usage: if/else  conditions

# if 1 == 1:
#     print("It one")

# Operators

# inp = int(input("Please provide a number: "))

# if inp < 10:
#     print("The number is less than 10")
# else:
#     print("The number is bigger than 10")

 # Class task 1:

#  Indentations ----> part of the python syntax
#  f string ----> gives ability to insert variable to your string

word = str(input("Please provide a word: "))   ## aKumoSolutions
length = len(word)
if length > 10:
    print(f"That's a long word. It has {length} characters")
else:
    print(f"The word has {length} characters")
    


# Class task2 :

num = int(input("Please provide a number: "))

if num > 0:
    if num  % 2 == 0:   ### 5 % 3 = 2
        print("Even")
    else:
        print("Odd")
else:
    print("Hey, give me positive number !!!")