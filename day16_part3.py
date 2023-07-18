name = input("Enter Your Name: ")

if name == "xyz":
    print("Your are Not Allowed to Take Admission.")
else:
    marks = int(input("Enter Your Marks: "))
    if marks >= 40:
        print("You are Eligible.")
    else:
        print("You are not Eligible.")
