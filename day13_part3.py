# Dictionary to Store Data and then update Value of Key

dic = {"Name": "Muhammad", "Address": "Lahore",
       "Contact": "Email"}
print("First Record\n", dic)
dic.update({"Contact": input("Enter Your Updated Contact: ")})
print("Updated Record\n", dic)


# Program to get 3 numbers from user then apply formula (a+b+ca\b(2a+3b))

a = float(input("Enter a Number 'a': "))
b = float(input("Enter a Number 'b': "))
c = float(input("Enter a Number 'c': "))
# formula = (a+b+(ca\b)(2a+3b))

formula = (a + b + ((c*a)/b) * ((2 * a) + (3 * b)))
print("Result is:", formula)

