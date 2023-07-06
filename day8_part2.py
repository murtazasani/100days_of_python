# Using Math Module


from math import sqrt
no = int(input("Enter a Number:"))
print(sqrt(no))

# Little Magic in Few Lines\


print("Number \t\t Square \t\t Cube")

for x in range(1, 10):
    square = int(x) ** 2
    cube = int(x) ** 3
    print(x, " \t\t\t ", square, "\t\t\t", cube)


# Calculate Area of Rectangle

length = float(input("Enter length: "))
width = float(input("Enter Width: "))

area_of_rectangle = length * width

print("Area of Rectangle is:", area_of_rectangle)




