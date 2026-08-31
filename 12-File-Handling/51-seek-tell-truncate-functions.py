# seek() func - it allows you to move the current position within a file to a specific point.
# the position is specified in bytes and you can move either forward or backward from current position.

with open('myFile5.txt', 'r') as f:
    # move to the 10th byte in file
    # print(type(f))
    f.seek(10)

    # read the next 5 bytes
    data = f.read(5)
    print(data)


# tell() func - it return the current position within a file, in bytes.
# this can be useful for keeping track of your location within the file or for seeking for a specific position relative to the current posiiton

with open('myFile5.txt', 'r') as f:
    # move to the 10th byte in file
    # print(type(f))
    f.seek(10)

    # read the next 5 bytes
    print(f.tell())
    data = f.read(5)
    print(data)


# truncate() function - when you open a file in python using the open fun, you can specify the mode in which you want to open a file.
# if you want to truncate the file to a specific size, you can use truncate()

with open('myFile5.txt', 'w') as f:
    f.write('Iron Man')
    f.truncate(5)

with open('myFile5.txt', 'r') as f:
    print(f.read())