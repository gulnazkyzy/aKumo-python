# Task 5: Number Type Identifier
# Take a single integer input and classify it as follows:
# If it’s positive and even, print "Positive Even"
# If it’s positive and odd, print "Positive Odd"
# If it’s negative and even, print "Negative Even"
# If it’s negative and odd, print "Negative Odd"
# If it’s zero, print "The number is zero"

num = int(input("Enter a number, please: "))

if num == 0:
    print("The number is zero")
elif num > 0:
    if num % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
else:
    if num % 2 == 0:
        print("Negative Even")
    else:
        print("Negative Odd")