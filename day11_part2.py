# Inheritance

class Person:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    def __str__(self):
        return f"{self.name} Person Object"

    def dummy(self):
        return self.name


class Student(Person):
    def __init__(self, name, dob, grade):
        super().__init__(name, dob)
        self.grade = grade

    def __str__(self):
        return f"{self.name} Student Object"

    def passing(self):
        return True if self.grade > 4 else False


Student1 = Student("Gulfam Khan", "11-05-1992", 2)
print(Student1.name, Student1.dob, Student1.grade)
print(Student1.passing())
print(Student1.dummy())


