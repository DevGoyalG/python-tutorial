# multiple inheritance - allows you to inherit attributes and methods from multiple parent classes
# can be useful in situations where a class needs to inherit functionality from multiple sources

# MRO (Method Resolution Order) - in case of multiple inheritance, 
# python follows MRO to resolve conflicts between methods or attributesfrom different parent class
# MRO determines the order in which parent classes are searched for attributes and methods

class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"The name is {self.name}")

class Dancer:
    def __init__(self, dance):
        self.dance = dance

    def show(self):
            print(f"The dance is {self.dance}")

class DancerEmployee(Employee, Dancer):
    def __init__(self, dance, name):
        self.dance = dance
        self.name = name


o = DancerEmployee("Kathak", "Natasha")
print(o.name)
print(o.dance)
o.show()

# MRO
print(DancerEmployee.mro())
