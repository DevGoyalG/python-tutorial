# Strings in Python

name = "Dev"
friend = "Rishabh"
anotherfriend = 'Narayan'
apple = 'He said, "I want to eat an apple'

print("Hello! " + name)
print(apple)

mango = '''He said,
Hi Dev
Hey I am good
"I want to eat an apple'''

print("Hello! " + name)
print(mango)

print(name[0])
print(name[1])
print(name[2])
# print(name[3])  #Throws an error

print("Lets use a for loop\n")
for character in name:
    print(character)

print("Lets use a for loop\n")
for character in apple:
    print(character)   