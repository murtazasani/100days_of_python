name = input("Enter Your Name: ")
age = int(input("Enter your age: "))

if age < 18:
    print(name, "you are not allowed to Participate in Voting.")
    af = 18 - age
    print("You will be eligible after", af, "Years.")
else:
    print(name, "you are Eligible for voting.")


no1 = int(input("Enter a Number: "))
no2 = int(input("Enter a 2nd Number: "))

print("Table of Number:", no1)
for i in range(1,11):
    number1 = no1 * i
    print(no1, "X", i, "=",number1)

print("Table of Number:", no2)
for i in range(1,11):
    number2 = no2 * i
    print(no2, "X", i, "=", number2)
