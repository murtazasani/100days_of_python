# Using Class

class Car:
    def __init__(self, hp, model, brand, year):
        self.horsepower = hp
        self.model = model
        self.brand = brand
        self.year = year

    def info(self):
        return f"{self.brand} {self.model} {self.year}"


car1 = Car(890, "Audi", "A4", 2022)
car2 = Car(1250, "Tesla", "G-4", 2023)
car3 = Car(1460, "Nissan", "M9", 2024)
print(car1.info())
print(car2.info())
print(car3.info())
