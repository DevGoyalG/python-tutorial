# readline() method - reads a single line from a file, if we want to read multiple file then we can use loops

# for read strings
f = open('myFile3.txt', 'r')
while True:
    line = f.readline()
    if not line:
        # print(line, type(line))
        break
    print(line)

# for read numbers
f = open('myFile4.txt', 'r')
i=0
while True:
    i=i+1
    line = f.readline()
    if not line:
            break
    m1 = line.split(",")[0]
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]
    print(f"Marks of student {i} in maths is: {m1}")
    print(f"Marks of student {i} in english is: {m2}")
    print(f"Marks of student {i} in hindi is: {m3}")
    
    print(line)


# writelines() methods - write a sequence of strings to a file

f = open('myFile3.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()