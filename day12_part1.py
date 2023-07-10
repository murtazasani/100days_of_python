# Get 6 numbers from user as tuple and then add them

lst = []

for i in range(1, 6):
    lst.append(int(input("Enter a Number: ")))

print(lst)

tup = tuple(lst)

s = 0
for i in tup:
    s += i
print("Sum of Numbers in Tuple is:", s)

