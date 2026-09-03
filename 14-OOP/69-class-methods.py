# Class Methods in Python #

# class methods - it is a type of method that is bound to the class and not the instance of the class

class Employee:
    company="Apple"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")
    
    def changeCompany(cls,newCompany):
        cls.company=newCompany

e1=Employee()
e1.name="Rishu"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.company)    # it print - Apple
 


class Employee:
    company="Apple"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")
    
    @classmethod
    def changeCompany(cls,newCompany):
        cls.company=newCompany

e1=Employee()
e1.name="Rishu"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.company)     # it print - Tesla
