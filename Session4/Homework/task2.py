# Task 2: Remove Duplicates from a List
# Ask the user to enter multiple words separated by spaces. Store them in a list and remove duplicate words while maintaining the original order.
# Example:
# Enter words: apple banana apple cherry banana apple  
# Filtered List: ['apple', 'banana', 'cherry']

# Take input from user (multiple repeated words)
# removes duplicated words

words = input("Please enter your words: ").split()
removed_duplicates = []         
for word in words:
    if word not in removed_duplicates:
        removed_duplicates.append(word)
print("Filtered List:", removed_duplicates)




# [root@Python Homework]# python3 task2.py
# Please enter your words: apple banana apple cherry banana apple
# Filtered List: ['apple', 'banana', 'cherry']
# [root@Python Homework]#