# Introduction to Lists in Python #

l1 = [3, 5, 6]
print(l1)
print(type(l1))
print(l1[0])
print(l1[1])
print(l1[2])

l = [3, 5, 6, "Devil", True, "Rishabh", 10, "Narayan"]
print(l)
print(type(l))
print(l[0])
print(l[1])
print(l[2])
print(l[3])
print(l[4])

l = [3, 5, 6, "Devil", True, "Rishabh", 10, "Narayan"]
print(l[-1])         # Negative Index
print(l[-2])
print(l[-3])
print(l[-4])
print(l[-5])

l = [3, 5, 6, "Devil", True, "Rishabh", 10, "Narayan"]
print(l[-3])         # Negative Index
print(l[len(l)-3])   # Positive Index
print(l[5-3])        # Positive Index
print(l[2])          # Positive Index

l = [3, 5, 6, "Devil", True, "Rishabh", 10, "Narayan"]
if 7 in l:
    print("Yes")
else:
    print("No")

l = [3, 5, 6, "Devil", True, "Rishabh", 10, "Narayan"]
if "Devil" in l:
    print("Yes")
else:
    print("No")

if "evil" in "Devil":           # Same thing apply for string as well
    print("Yes")
else:
    print("No")

l = [3, 5, 6, "Devil", True, "Rishabh", 10, "Narayan"]
print(l)
print(l[:])
print(l[1:-1])
print(l[1:4])
print(l[1:4:2])
print(l[1:6])
print(l[1:6:2])
print(l[1:8])
print(l[1:8:2])
print(l[1:8:3])

lst = [i for i in range(4)]
print(lst)
lst = [i*i for i in range(4)]
print(lst)
lst = [i+i for i in range(4)]
print(lst)

lst = [i for i in range(10) if i%2 ==0]
print(lst)
lst = [i*i for i in range(10) if i%2 ==0]
print(lst)