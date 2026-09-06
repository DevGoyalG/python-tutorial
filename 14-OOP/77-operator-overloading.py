# operator overloading - that allows you to redefine the behavior of mathematical and comparison operators for custom data types
# this means that you can use the standard mathematical operators (+,-,*,/ etc) and comparison operators (>,<,== etc) 
# in your own classes just as you would for built-in data types like int, float and str.


class Vector:
    def __init__(self, i, j, k): 
        self.i=i
        self.j=j
        self.k=k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(self, x):          # operator overloading
        return Vector(self.i + x.i, self.j + x.j, self.k + x.k)

v1 = Vector(3,4,5)
print(v1)

v2 = Vector(1,2,3)
print(v2)

print(v1+v2)
print(type(v1+v2))     