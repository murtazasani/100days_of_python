# Nested for loop

meal = ["Pizza", "Burger", "Hot Wings", "Sandwich"]
drink = ["Water", "Juice", "Coke", "Red Bull"]
dessert = ["Ice Cream", "Cake", "Fruit Salad"]

for m in meal:
    for d in drink:
        for ds in dessert:
            print("I will like to have " + m + " as Meal" + " I also want " + d +
                  " as drink " + "and i would like to have " + ds + " as Dessert.")

