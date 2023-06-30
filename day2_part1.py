# In this Project we will use functions to take orders of Restaurant Customers.


for _ in range(2):
    def person1(name):
        print(name + ": How Can I Help You Sir!")


    def person2(name, food, drink, dessert):
        name = input("What's Your Name: ")
        food = input("What You would Like to Eat: ")
        drink = input("What You Would like to drink: ")
        dessert = input("What dessert do you want: ")


    def person1_2(name):
        print(name + "ThankYou Sir. \nNext Customer Please. ")


    person1("Cashier")
    person2("name", "food", "drink", "dessert")
    person1_2("Cashier ")

