# Decorators in Python #

# decorator - are a powerful and versatile tool that allow you to modify the behavior of func and methods.

def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks for using this function.")
    return mfx

@greet
def hello():
    print("Hello World")

@greet
def add(a,b):
    print(a+b)

# greet(hello)()    # basic way
hello()             # best way
# greet(add)(1,2)
add(1,2)