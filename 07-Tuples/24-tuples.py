# Tuples in Python #

tup = (1)               
print(type(tup))          # Result will be "int"
print(tup)

tup = (1,)                # Use comma
print(type(tup))          # Result will be "tuple"
print(tup)

tup = (1, 5, 6)
print(type(tup))
print(tup)

# tup = (1,)
# tup[0] = 90               # no add in tupple
# print(tup)                # not executable

tup = (1, 2, 76, 123, 55, "Devil", True)
print(type(tup))
print(tup)
print(len(tup))
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])

print(tup[-1])
print(tup[-2])
print(tup[-3])
print(tup[-4])

if 123 in tup:
    print("Yes 123 is present in this tuple")
else:
    print("Not")

tup2 = tup[1:4]
print(tup2)