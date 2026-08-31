# Classes and Objects in Python

# class - it is a blueprint or a template for creating objects, providing initial values for state (member var or attributes) 
# and implementation of behavior (member func or methods)

# object - it is the instance of the class used to access the properties of the class

# self - self parameter is a reference to the current instance of the class and i used to access variables that belongs to the class

class Person:                   # class
    name = "Dev Goyal"
    occupation = "Student"
    networth = 10

a = Person()                    # object
print(a.name)


class Person:
    name = "Dev Goyal"
    occupation = "Student"
    networth = 10

a = Person()
a.name = "Devil"
a.occupation = "Accountant"
print(a.name, a.occupation)


class Person:
    name = "Dev Goyal"
    occupation = "Student"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
a.info()


class Person:
    name = "Dev Goyal"
    occupation = "Student"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
b = Person()
c= Person()
a.name = "Devil"
a.occupation = "Accountant"

b.name = "Nitika"
b.occupation = "HR"

a.info()
b.info()
c.info()

