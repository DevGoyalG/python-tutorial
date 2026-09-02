# Inheritance - when a class derives from another class. 
# the child class will inherit all the public and protected props and methods from parent class
# in addition, it can have its own props and methods


# parent class
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"Name of employee: {self.id} is {self.name}")

# child class
class Programmer(Employee):
    def showLanguage(self):
        print("The default lang is Python")


e1 = Employee("Iron Man", 45)
e1.showDetails()

e2 = Employee("Captain America", 18)
e2.showDetails()

e3 = Programmer("Thor", 7)
e3.showLanguage()