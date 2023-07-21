# To Check if year is Leap

lis = []
for x in range(5):
    year = int(input("Enter the Year: "))
    lis.append(year)

print(lis)

for x in lis:
    if x % 4 == 0:
        print(x, "Year is Leap.")






