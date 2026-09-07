# multilevel inheritance - where a derived class inherits from another derived class.
# it allows you to build a heirarchy of classes where one class builds upon another, leading to a more specialized class


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def show(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")


class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed

    def show(self):
        Animal.show(self)
        print(f"Breed: {self.breed}")


class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed="Golden Retriever")
        self.color = color

    def show(self):
        Dog.show(self)
        print(f"Color: {self.color}")


o = GoldenRetriever("Tommy", "Black")
o.show()

print(GoldenRetriever.mro())