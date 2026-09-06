# Magic / Dunder methods - these are special methods that you can define in your classes, 
#                          and when invoked, they give you a powerful way to manipulate objects and their behaviour.
#                          from the double underscores surrounding their names are powerful tools that
#                          allow you to customize the behavious of your classes
# __init__ , __str__ , __repr__ , __len__ , __call__

class Employee:
    def __init__(self, name):
        self.name = name

    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i

e = Employee("Iron Man")
print(e.name)
print(len(e))