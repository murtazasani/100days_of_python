num1 = int(input("Enter the first Number: "))
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
elif op == "%":
    print(num1 % num2)
else:
    print("Invalid Operator Please Enter Valid Operator +, -, /, *, %")
