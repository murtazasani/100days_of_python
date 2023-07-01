# Checking The Richest Person

name1 = input("What's Your Name: ")
salary1 = input(name1 + " How much Money do you have? ")

name2 = input("What's Your Name: ")
salary2 = input(name2 + " How much Money do you have? ")

name3 = input("What's Your Name: ")
salary3 = input(name3 + " How much Money do you have? ")

if float(salary1) > float(salary2) and float(salary1) > float(salary3):
    print("Person 1 is Richest")
elif float(salary2) > float(salary1) and float(salary2) > float(salary3):
    print("Person 2 is Richest")
elif float(salary3) > float(salary2) and float(salary3) > float(salary1):
    print("Person 3 is Richest")
