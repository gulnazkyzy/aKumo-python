# Task 2:
# Take an input and count the occurrences of each character.
# Input: programming
# Output: {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}


inp = input("Please provide the input: ")  # Get input -->   programming
list = {} 

for char in inp: 
    if char in list:   # this line checks if the character exist in the list
        list[char] += 1 
    else:
        list[char] = 1 
print(list)