# Task 5: Print a Word in a Pyramid Shape
# Input:
# Enter a word: CODE

# Output:
# C
# CO
# COD
# CODE

# Step 1: Take input from the user

word = input("Enter a word: ") # CODE

for i in range(1, len(word) + 1):
    print(word[:i])