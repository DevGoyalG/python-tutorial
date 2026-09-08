# hybrid inheritance - it is a combination of multiple inheritance and single inheritance 


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Person(Human):
    def __init__(self, name, age, address):
        Human.__init__(self, name, age)
        self.address = address

    def show(self):
        Human.show(self)
        print(f"Address: {self.address}")     


class Program(Human):
    def __init__(self, program_name, duration):
        self.program_name = program_name
        self.duration = duration

    def show(self):
        print(f"Program Name: {self.program_name}")
        print(f"Duration: {self.duration}")  


class Student(Person):
    def __init__(self, name, age, address, program):
          Person.__init__(self, name, age, address)
          self.program = program

    def show(self):
        Person.show(self)


p = Program("AIML", 4)
s = Student("Dev", 22, "India", p)
s.show()



# hierarchical inheritance - where multiple subclasses inherit from a single base class
# in other words, a single base class acts as a parent class for multiplesubclasses
# this is a way of establishing relationships between classes in a hierarchical manner 


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Student(Human):
    def __init__(self, name, age, course):
        Human.__init__(self, name, age)
        self.course = course

    def show(self):
        Human.show(self)
        print(f"Course: {self.course}")


class Teacher(Human):
    def __init__(self, name, age, subject):
        Human.__init__(self, name, age)
        self.subject = subject

    def show(self):
        Human.show(self)
        print(f"Subject: {self.subject}")


class Employee(Human):
    def __init__(self, name, age, department):
        Human.__init__(self, name, age)
        self.department = department

    def show(self):
        Human.show(self)
        print(f"Department: {self.department}")


s = Student("Dev", 22, "AIML")
t = Teacher("Rahul", 35, "Python")
e = Employee("Amit", 28, "IT")

s.show()
print()

t.show()
print()

e.show()