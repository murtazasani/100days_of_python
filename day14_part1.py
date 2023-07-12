# Program to store 5 numbers in list and then show their Sum

num1 = float(input("Enter a Number: "))
num2 = float(input("Enter a Number: "))
num3 = float(input("Enter a Number: "))
num4 = float(input("Enter a Number: "))
num5 = float(input("Enter a Number: "))
list1 = [num1, num2, num3, num4, num5]
sum1 = num1 + num2 + num3 + num4 + num5

print(list1)
list1.clear()
list1.append(sum1)
print(list1)
