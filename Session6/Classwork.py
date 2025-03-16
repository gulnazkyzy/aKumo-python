students = {
    "101": {
        "name": "Alice Johnson",
        "age": 20,
        "grade": "A",
        "courses": ["Math", "Physics", "Computer Science"],
        "attendance": 95
    },
    "102": {
        "name": "Bob Smith",
        "age": 21,
        "grade": "B",
        "courses": ["History", "Literature", "Political Science"],
        "attendance": 88
    },
    "103": {
        "name": "Charlie Brown",
        "age": 19,
        "grade": "A-",
        "courses": ["Biology", "Chemistry", "Physics"],
        "attendance": 92
    },
    "104": {
        "name": "Diana Adams",
        "age": 22,
        "grade": "A+",
        "courses": ["Economics", "Statistics", "Business"],
        "attendance": 80
    },
    "105": {
        "name": "Ethan Green",
        "age": 20,
        "grade": "B+",
        "courses": ["Computer Science", "Mathematics"],
        "attendance": 90
    }
}

# Task 1: that prints the user id and prints the name of the student in the following format
# 101: Alice Johnson 
# 102: Bob Smith
# ....
# 105: Ethan Green

# dictionary = {key: value["name"]for key, value in students.items()}

# for key, value in students.items():
#     print(f'{key}: {value["name"]}')


# Class task2
# print only students that grades are A (A-, A)
# 101: Alice Johnson
# 103: Charlie Brown

# for key, value in students.items():
#     # in 
#     if 'A' in value["grade"]:
#         print(f'{key}: {value["name"]}')


    


# Class Task3
# Ask user for an input of course
# Print the students that are taking course
# Input: Computer Science
# Output: 
# 101: Alice Johnson
# 105: Ethan Green

# inp = input("Input: ")

# for key, value in students.items():
#     if inp in value["courses"]:
#         print(f'{key}: {value["name"]}')



# Class task 4

# Create function that takes an integer input and prints if it's Odd or Even
# my_func(10) ---> This is even number --> str
# my_func(5) ---> This is odd number --> str

# def my_func(num):
#     if num % 2 == 0:
#         print("This is even number")
#     else:
#         print("This is odd number")

# my_func(4)
# my_func(9)


# What is the difference between print() and return


# Class task 5

# Create function that takes a list of integers
# return the list of even numbers
# Input --> [1,2,3,4,5,6,7,8,9,10]
# Output --> [2,4,6,8,10]

def checkEven(lst_int):
    even_lst = []
    for i in lst_int:
        if i % 2 == 0:
            even_lst.append(i)

    return even_lst

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst2 = [46, 12, 97, 53, 40, 1, 37]
lst3 = [311, 56, 76, 89, 91, 93, 100]

print(checkEven(lst))
print(checkEven(lst2))
print(checkEven(lst3))


# Class task 6

# Take an input of word and character and return an index of this character
# if no character is available return "No such character"
# 
# Input: my_func('akumosolutions', 'l')
# Output: 7
# 
# Input: my_func('akumosolutions', 'z')
# Output: "No such character"


def characterChecker(word, character):
    if character in word:
        return word.index(character)
    else:
        return "No such character"

print(characterChecker("akumosolutions","l"))
print(characterChecker("akumosolutions","z"))
