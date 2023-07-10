

try:
    number1 = input("Enter a Number: ")
    number1 = float(number1)

except:
    print("You have ValueError. \nNote:(ValueError) occur when you entered text but it required Number.")
    number1 = input("Enter a Number: ")

try:
    number2 = input("Enter a Another Number: ")
    number2 = float(number2)

except Exception as err:
    print(err)
    number2 = input("Enter a Another Number: ")

if number1 < number2:
    print("Number 2 is Greater.")
elif number1 > number2:
    print("Number 1 is Greater.")
else:
    print("Number 1 is Equal to Number 2.")
