# Classes and Objects in Python #

class Person:
    name = "Dev Goyal"
    occupation = "Student"
    networth = 10

a = Person()
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

