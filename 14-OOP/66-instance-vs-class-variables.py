# Instance Variables vs Class Variables in Python #

# instance var - Instance variables belong to a specific object. Each object maintains its own independent copy of the variable. 
#                Changing it on one object does not affect any other object
# class var    - Class variables belong to the class itself. They are shared by all instances of that class. 
#                If you modify the class variable via the class, the change is reflected across all existing and future objects

class Employee:
    def __init__(self,name):
        self.name=name             # Instance Variable
        self.raise_amount=0.02

    def showDetails(self):
        print(f"The name of the Employee is {self.name} and the raise amount is {self.raise_amount}")

emp1=Employee("Rishabh")
emp1.showDetails()
# Employee.showDetails(emp1)
emp2=Employee("Narayan")
emp2.showDetails()
emp1.raise_amount=0.3
emp1.showDetails()


class Employee:
    companyName="Apple"                 # Class Variable
    noOfEmployees=0
    def __init__(self,name):
        self.name=name
        self.raise_amount=0.02
        Employee.noOfEmployees+=1

    def showDetails(self):
        print(f"The name of the Employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}")

emp1=Employee("Rishabh")
emp1.raise_amount=0.3
emp1.companyName="Apple India"
emp1.showDetails()
Employee.companyName="Google"
print(Employee.companyName)
# Employee.showDetails(emp1)
emp2=Employee("Narayan")
emp2.companyName="Microsoft"
emp2.showDetails()
