# Set Methods in Python #

s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
print(s1.union(s2))          # union of two sets

print(s1, s2)                # print both sets

s1.update(s2)                # update s1
print(s1, s2)                # print updated s1 and s2

cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

cities3 = cities1.union(cities2)
print(cities3)

cities3 = cities1.intersection(cities2)           # intersection of two sets
print(cities3)

cities1.intersection_update(cities2)              # update c1
print(cities3)

cities3 = cities1.symmetric_difference(cities2)   # symmetric difference = (c1 union c2) - (c1 intersection c2)
print(cities3)

cities3 = cities1.difference(cities2)             # difference = c1 - c2
print(cities3)

print(cities1.isdisjoint(cities2))

print(cities1.issuperset(cities2))
cities3 = {"Seoul", "Madrid", "Kabul"}
print((cities1.issuperset(cities3)))

cities3 = {"Tokyo", "Madrid", "Delhi"}
print((cities1.issuperset(cities3)))

cities3 = {"Tokyo", "Madrid", "Delhi"}
print((cities3.issubset(cities1)))

cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities1.add("Helsinki")
print(cities1)

cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities1.remove("Tokyo")
print(cities1)

# cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities1.remove("Tokyo2")                                    # raise error because "Tokyo2" is not found
# print(cities1)

cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities1.discard("Tokyo2")                                   # not show error and run next code
print(cities1)

cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities1.pop()
print(cities1)                                              # randomly removed a value
print(item)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# del cities                                                # raise error because cities are deleted
# print(cities)                                     

info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")