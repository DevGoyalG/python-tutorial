# Strings Slicing and Operations on Strings in Python #

names = "Dev, Rishabh"
print(names[0:3])
print(len(names))

fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.")

print(len1)
print(fruit[0:4]) # including 0 but not 4
print(fruit[:4])  # including 1 but not 4
print(fruit[1:4])
print(fruit[:])

print(fruit[0:len(fruit)-3])
print(fruit[0:-3])
print(fruit[-1])
print(fruit[:-1])
print(fruit[-3:-1])