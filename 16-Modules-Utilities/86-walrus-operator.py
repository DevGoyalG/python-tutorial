# walrus operator - is a new addition in Python 3.8 and allows you to assign a value to a variable within an expression. 
# This can be useful when you need to use a value multiple times in a loop, but don't want to repeat the calculation.
# it is represented by " := " syntax and can be used in a variety of contexts including while loops and if statements.


a = True
print(a)
print(a:=False)


nums = [1,2,3,4,5]
while(n := len(nums)) > 0:
    print(nums.pop())

# simple
foods = list()
while True:
    food = input("What food do you like?: ")
    if food == "quit":
        break
foods.append(food)

# by walrus
foods1 = list()
while (food1 := input("What food do you like?: ")) != "quit":
    foods1.append(food1)