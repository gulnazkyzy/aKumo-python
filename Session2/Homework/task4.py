# Task 4: Password Strength Checker
# Ask the user for a password input. Check and print:
# "Strong password" if the length is at least 8 characters and contains both letters and numbers.
# "Weak password" otherwise.

passw = input("Please provide your password: ")

if len(passw) >=8:
    if (passw.isdigit()) or (passw.isalpha()):
        print("It is a weak password")
    else:
        print("It is a strong password: ")
else:
    print("This is weak password")
