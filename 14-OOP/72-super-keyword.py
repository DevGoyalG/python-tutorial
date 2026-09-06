# super() keyword - is used to refer to the parent class. it is specially useful when a class 
#                   inherits from multiple parent classes and you want to call a method from one of the parent class

class ParentClass:
    def parent_method(self):
        print("Parent method 1")

class ChildClass(ParentClass):
    def parent_method(self):
        print("Parent method 2")
    def child_method(self):
        print("Child method")
        super().parent_method()


child_object = ChildClass()
child_object.child_method()
child_object.parent_method()