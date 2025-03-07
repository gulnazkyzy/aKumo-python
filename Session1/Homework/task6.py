# Task 6: Palindrome Checker
# Ask the user to enter a word and check whether it reads the same forward and backward (e.g., "madam" is a palindrome).

# The answer should return True or False

word = input("Please enter a word: ")
word = word.lower()
length = len(word)
backword = ""
for i in range(length - 1, -1, -1):
    backword += word[i]
if word == backword:
    print(True)
else:
    print(False)