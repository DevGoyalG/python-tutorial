# List Methods in Python #

l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)

l.append(7)             # add new element in list at last
print(l)

l.sort()                # change list into ascending order
print(l)

l.sort(reverse=True)    # change list into descending order
print(l)

l.reverse()             # change list into descending order
print(l)

l.insert(1, 899)        # add 899 with 1
print(l)

n = [900, 1000, 1100]   
l.extend(n)             # merge two lists
print(l)

n = [900, 1000, 1100]
k = l + n               # merge two lists
print(k)

print(l.index(6))       # index of element 6

print(l.count(1))       # number of counting of "1"

l = [11, 45, 1, 2, 4, 6, 1, 1]
m = l
m[0] = 0
print(l)                # add some element on some index

l = [11, 45, 1, 2, 4, 6, 1, 1]
m = l.copy()            # add some element on some index
m[0] = 0
print(l)