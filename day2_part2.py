# Use of functions and loop and also used if statement to take orders.

N = input("How many person orders you wanna take at a time: ")

for x in range(int(N)):
    def person1(name):
        print(name + ": How Can I Help You Sir!")


    def person2(name, food, drink, dessert):
        c_name = input("What's Your Name: ")
        if c_name == "":
            c_name = "Mr Nobody"
        food = input(c_name + " Would you Like to Eat: ")
        if food == "yes" or food == "Yes" or food == "YES":
            fd = input("What would u like to Eat: ")
        drink = input(c_name + " Would you like to drink: ")
        if drink == "yes" or drink == "Yes" or drink == "YES":
            dr = input("What u would like to drink: ")
        dessert = input(c_name + " Would u like dessert: ")
        if dessert == "yes" or dessert == "Yes" or dessert == "YES":
            dsrt = input("What u would like in dessert: ")

    def person1_2(name):
        print(name + "ThankYou Sir. ")


    person1("Cashier")
    person2("name", "food", "drink", "dessert")
    person1_2("Cashier: ")

print("We are Closed Now")