# 5 Numbers from user and store in a list and then Remove all elements

lst = []
for i in range(5):
    num = int(input("Enter a Number: "))
    lst.append(num)

print("This is the list\n" + str(lst))
lst.clear()
print(lst)
