# Task 2: Convert a Sentence to Abbreviations
# Write a function that takes a sentence as input and returns an abbreviation using the first letter of each word in uppercase.
# Example:
# print(abbreviate("Central Processing Unit"))

# Output:
# "CPU"

def abbreviate(word):
    lst_of_words = word.split()   # converts string to list ---> ' '
    final = ""
    for word in lst_of_words:
        final += word[0].upper()

    return final

inp = input("Input: ")
print(abbreviate(inp))

#print(abbreviate("Central Processing Unit"))


# [root@Python Homework]# python3 task2.py
# Input: Central Processing Unit
# CPU
# [root@Python Homework]# 