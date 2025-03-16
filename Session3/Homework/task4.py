# Task 4: Password Verification (Limited Attempts)
# secret password = Python123
# Input:

# Enter the password: hello
# Wrong password. Try again.

# Enter the password: python
# Wrong password. Try again.

# Enter the password: Python123
# Access Granted!

secret_passw = "Python123"
while True:
     user_pass = input("Please enter your password: ")
     if user_pass == secret_passw:
        print("Access Granted!")
        break  
else:
    print("This is a wrong password. Please try again.")