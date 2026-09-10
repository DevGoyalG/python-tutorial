# generators - are a special type of funcs that allows you to create an iterable sequence of values.
# a generator func returns a generator object, which can be used to generate the values one by one as you iterate over it.
# you can create generator func by using "yield" statement


def my_generator():
    for i in range(5):
        yield i

gen = my_generator()

# simple for print
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# OR for print
for j in gen:
    print(j)