# Authentication Access granted or Blocked

pass1 = "pass123"
your_ans = ""
try1 = 0
no_of_try = 4
max_try = "Not Reached"
while your_ans != pass1 and max_try != "Reached":
    if try1 < no_of_try:
        your_ans = input("What is Your Password: ")
        try1 += 1
    else:
        max_try = "Reached"

if max_try == "Reached":
    print("Account Blocked")
else:
    print("Access Granted")

