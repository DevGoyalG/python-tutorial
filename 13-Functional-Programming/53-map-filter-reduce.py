# map func - it applies a func to each element in a sequence and returns a new sequence containing the transformed elements

# list of numbers
l = [1,2,3,4,5]
# double each number using map fun
doubled = list(map(lambda x:x*2, l))
print(doubled)


# filter func - it filters a sequence of elements based on a given predicate and return a new sequence containing only the elements that meet the predicate

# list of numbers
l = [1,2,3,4,5]
# get only the even no. using the filter func
evens = list(filter(lambda x:x%2==0, l))
print(evens)


# reduce - it is a higher order func that applies a func to a sequence and returns a single value.
# it is a part of functools module in python

from functools import reduce
# list of numbers
l = [1,2,3,4,5]
# calculate sum of n. using reduce func
sum = reduce(lambda x,y:x+y, l)
print(sum)