# Dictionaries in Python #

dic = {
    "Devil": "Human Being",
    "Spoon": "Object"
}

print(dic["Devil"])
print(dic["Spoon"])

dic = {
    28: "Dev",
    62: "Rishabh Saini",
    27: "Darshita"
}

print(dic[27])
print(dic[28])

info = {"name":"Dev", "age":19, "eligible":True}
print(info)

print(info["name"])                  # type 1
print(info.get("name"))              # type 2 (result same)

# print(info["eligible2"])              # raise error
print(info.get("eligible2"))          # dont raise error...print None
 
info = {"name":"Dev", "age":19, "eligible":True}
print(info)
print(info.keys())
print(info.values())

for key in info.keys():
    # print(info[key])
    print(f"The value corresponding to the key {key} is {info[key]}")

print(info.items())

for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")