# Task 3
# Take an input of list of numbers, find and print the unique numbers.
# Input: [1, 2, 2, 3, 4, 4, 5]
# Output: 1, 3, 5

# lst_of_num = [1, 2, 2, 3, 4, 4, 5]
# temp_dict = {}
# filtered_lst = []

# for i in lst_of_num:
#     temp_dict[i] = 0

numbers = input("Please enter your numbers: ").split()  
print(numbers)
new_list = []
for i in numbers:
    if numbers.count(i) == 1:
       new_list.append(i)
print(", ".join(new_list))