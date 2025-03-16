# Task 2: Reverse a Word using for loop (please don’t reverse a string using word[::-1])
# Input:
# Enter a word: Python
# Output:
# Reversed Word: nohtyP

# Take input from user. Input word is Python

word = input("Please enter the word: ")  
reversed_word = ""
for char in word:
    reversed_word = char + reversed_word 
print("Reversed Word:", reversed_word)



# [root@Python ~]# cd aKumo-python/Session3/Homework/
# [root@Python Homework]# ls
# task1.py  task2.py  task3.py  task4.py  task5.py
# [root@Python Homework]# python task2.py
# Please enter the word: Python
# Reversed Word: nohtyP
# [root@Python Homework]# 