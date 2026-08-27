# Operations on Tuple in Python #

countries = ("Spain", "Italy", "England", "Germany")
temp = list(countries)
temp.append("Russia")            # add items
temp.pop(3)                      # remove items
temp[2] = "Finland"              # change items
countries = tuple(temp)
print(countries)

countries = ("Pakistan", "Afghanistan", "Bangladesh", "SriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)

tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = tuple1.count(3)                     # How many times does 3 occur?
print("Count of 3 in tuple1 is: ", res)

tuple1 = (0, 1, 2, 35, 2, 3, 1, 3, 2)
res = tuple1.index(3)                     # Where does 3 appear first?
print("Index of 3 in tuple1 is: ", res)

tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
# tuple.index(value, start, end)
res = tuple1.index(3, 4, 8)               # indexing of 3 (Search within a specific range)
print("Count of 3 in tuple1 is: ", res)

tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = len(tuple1)
print(res)