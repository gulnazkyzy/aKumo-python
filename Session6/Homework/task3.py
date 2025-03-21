# Task 3: Find Common Elements in Two Lists
# Write a function that takes two lists as input and returns a list containing only the common elements (without duplicates).
# Example:
# print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))  
# Output:
# [3, 4]

# Version1 

def two_list(list1, list2):
    common = []

    for i in list1: 
        if i in list2:
            if i not in common:
              common.append(i)
    return common
list1 = input("Please enter the first list of numbers: ").split()
list2 = input("Please enter the second list of numbers: ").split()

result = two_list(list1, list2)
print(result)



# [root@Python Homework]# python3 task3.py
# Please enter the first list of numbers: 1 2 3 4 
# Please enter the second list of numbers: 3 4 5 6 
# ['3', '4']
# [root@Python Homework]# 


