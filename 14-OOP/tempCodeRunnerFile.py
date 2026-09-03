class Employee:
    def __init__(self):
        self.__name = "Dev"

a = Employee()
# print(a.__name)                # cannot be accessed directly
print(a._Employee__name)    