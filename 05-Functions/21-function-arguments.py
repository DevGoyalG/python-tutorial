# Function Arguments in Python #

def average(a,b):
    print("The avergae is: ", (a+b)/2)

average(2,8)

def average(a=9,b=1):
    print("The avergae is: ", (a+b)/2)

# average(2,8)
average()

def average(a=9,b=1):
    print("The avergae is: ", (a+b)/2)

# average(2,8)
average(1,5)

def average(a=9,b=1):
    print("The avergae is: ", (a+b)/2)

# average(2,8)
average(5)

def name(fname, mname = "Dev", lname = "Goyal"):
    print("Hello", fname, mname, lname)

name("Mr.")
name("Mr.", "Rishabh")
name("Mr.", "Rishabh", "Saini")

def average(a=9,b=1):
    print("The avergae is: ", (a+b)/2)

# average(2,8)
average(b=9,a=21)

def average(a,b,c=3):
    print("The avergae is: ", (a+b+c)/3)

# average(2,8)
average(b=9,a=21)

def average(*numbers):
    # print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    print("Average is: ", sum/len(numbers))

average(5,6,7,8,9,10)

def name(**name):
    print(type(name))
    print("Hello", name["fname"], name["mname"], name["lname"])

name(mname = "Devil", lname = "Sir", fname = "Mr.")

def average(*numbers):
    # print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    # print("Average is: ", sum/len(numbers))
    return sum/len(numbers)

c = average(5,6,7,8,9,10)
print(c)

def average(*numbers):
    # print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    # print("Average is: ", sum/len(numbers))
    # return sum/len(numbers)

c = average(5,6,7,8,9,10)
print(c)

def average(*numbers):
    # print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    # print("Average is: ", sum/len(numbers))
    return 7                      # First return will be execute
    return sum/len(numbers)

c = average(5,6,7,8,9,10)
print(c)