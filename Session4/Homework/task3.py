# Task 3: Find the Longest Word in a List
# Ask the user to enter a list of words. Find and print the longest word from the list.
# Example:
# Enter words: Python Java JavaScript C  
# Longest word: JavaScript


# This first line takes input from user.

words = input("Please enter your words: ").split() # Python Java JavaScript C 
longest_word = words[0]  
for word in words:  
    if len(word) > len(longest_word):  
        longest_word = word  
print("Longest word: ", longest_word)




# [root@Python Homework]# python3 task3.py
# Please enter your words: Python Java JavaScript C
# Longest word:  JavaScript
# [root@Python Homework]#