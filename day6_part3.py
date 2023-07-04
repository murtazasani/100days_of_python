# Some functions on Dictionary

dicti = {
    "Name": ["Ali"], "Age": 32, "Gender": "Male", "Phone": +923015426891
}
key = input("What information do you wanted to Know: ").capitalize()
result = dicti.get(key, "This Person Does Not Exists")

print(result)

print(dicti["Name"].insert(0, "Rizwan"))
print(dicti)

# Comparing Ages

m_age = 25
age = int(input("Enter Your Age: "))

if age<m_age:
    print("You're Younger than me.")
elif age > m_age:
    print("You're Older than me.")
else:
    print("We are of Same Age.")
