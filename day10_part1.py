# Basic Calculator

num1 = int(input("Enter a Number: "))
num2 = int(input("Enter the 2nd Number: "))
op = input("Enter the operator: ")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Sorry! Enter the basic Operator")
