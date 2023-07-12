# Array to store 5 number and then Sum them.

import array as arr

a = arr.array('i', [])
for i in range(5):
    a.append(int(input("Enter the Number: ")))
print(a)

s = 0
for j in range(5):
    s += a[j]
print("Sum of Array elements is: ", s)

print("Maximum Number in our Array is:", max(a))
print("Minimum Number in our Array is:", min(a))
