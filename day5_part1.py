# Some List Functionss

lis = [29, 1, 59, 39, 98]
lis1 = ["mike", 34, 19, 20.4]

lis.append("apple")
print(lis)

lis.insert(3, 11)
print(lis)

lis.extend([1, 2, 3, 4, 5])
print(lis)

lis.extend(lis1)
print(lis)

print(lis.index("mike"))

print(lis.count(1))

lis.remove("apple")
print(lis)

lis.pop(3)
print(lis)

lis.reverse()
print(lis)

lis.remove("mike")
print(lis)

# Sort in ascending order
lis.sort()
print(lis)

# Sort in descending order
lis.sort(reverse=True)
print(lis)
