# access modifiers / specifiers - are used to limit the access of class variables and class methods
# outside of class while implementing the concepts of inheritance

# types:-
# 1. public    : Members declared as public are accessible from anywhere in the program, both inside and outside the class
# 2. private   : Members declared as private can only be accessed from within the exact same class where they are defined.
# 3. protected : Members declared as protected can be accessed within the class itself and by 
#                any sub-classes or derived classes through inheritance. They are hidden from unrelated external code


class Employee:
    def __init__(self):
        self.__name = "Dev"

a = Employee()
# print(a.__name)                # cannot be accessed directly
print(a._Employee__name)         # can be accessed indirectly