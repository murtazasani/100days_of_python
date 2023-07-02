# Exception Handling

for x in range(3):
    try:
        a = int(input("Enter Number: "))
        print(1 + a)
    except ValueError:
        print("Please write a valid Number.")


