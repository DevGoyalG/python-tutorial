# is vs == both are comparison operator
# is - compare the identity of 2 objects
# == - compare the value of objects 

a = "dev"
b= "dev"
print(a==b)     # True
print(a is b)   # True

c = 45
d = 45
print(c==d)     # True
print(c is d)   # True

e = [1,2,3]
f = [1,2,3]
print(e==f)     # True
print(e is f)   # False