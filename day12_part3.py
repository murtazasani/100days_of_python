# Storing elements in empty tuple and then clearing.

lst = []
for i in range(5):
    num = int(input("Enter a Number: "))
    lst.append(num)

tup = tuple(lst)
print("This is the Tuple\n" + str(tup))

lst1 = list(tup)
lst1.clear()
tup1 = tuple(lst1)

print("This is the Empty Tuple\n" + str(tup1))
