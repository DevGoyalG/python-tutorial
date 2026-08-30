# local vs global variables

# Local Variables:  local variables are defined inside a function and can only be accessed within that function
# Global Variables: global variables are defined outside all functions and can be accessed anywhere in the program

# # BEFORE
# x=10 # global var

# def hello():
#     y=5 # local var
#     print(y)

# hello()

# print(x)
# print(y) # this will cause an error because y is a local var and is not accessible outside of the function hello()


# AFTER
x=4 # global var

def hello():
    global x
    x=4 # this will change the value of global var x
    y=5 # local var
    print(y)

hello()

print(x)
print(y) # this will cause an error because y is a local var and is not accessible outside of the function hello()