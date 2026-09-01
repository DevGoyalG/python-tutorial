# Constructors in Python

class Person:
    def __init__(self,n,o):
        print("Hey I am a person")
        self.name=n
        self.occ=o
    # self.name=name
    # name="Devil"
    # occ="Developer"

    def info(self):
        print(f"{self.name} is a {self.occ}")

a=Person("Dev", "Developer")
b=Person("Yashi", "HR")
# c=Person()
a.info()
b.info()

# print(a.name)
# a.name="Yashi"
# a.occ="HR" 
# a.info()



