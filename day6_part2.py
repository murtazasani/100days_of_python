# Simple Code for Person's Initials and Some Details


f_name = input("What's Your First Name: ")
m_name = input("What is Your Middle Name: ")
l_name = input("What is Your Last Name: ")

print("Your Initials are", f_name[0], m_name[0], l_name[0])


lot_number = "037-00901-00027"
print("Country Code =", lot_number[:3])
print("Product Code =", lot_number[4:9])
print("Batch Number", lot_number[10:])

# Printing Month for DoB Using List and Tuples

months = ('january', "February", "March", "April0", "May", "June", "July", "August", "September", "October", "November", "December")
lis = input("What is Your Birthday in DD-MM-Year: ")
index = int(lis[3:5])-1
bd_month = months[index]
print("You Were Born in", bd_month)
