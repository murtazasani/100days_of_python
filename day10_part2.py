# Basic Login Setup


print("Create Account Now")
username = input("Enter Username: ")
password = input("Enter Password: ")

print("Account Created Successfully. \nLogin Now!")

username2 = input("Enter Username: ")
password2 = input("Enter Password: ")

if username2 == username and password2 == password:
    print("Successfully Logged In.")
elif username2 == username and password2 != password:
    print("Password Incorrect.")
elif username2 != username and password2 == password:
    print("Username is Incorrect.")
else:
    print("Username and Password are Incorrect.")
