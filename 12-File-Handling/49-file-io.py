# read(r) - open a file for reading only and gives an error if file does not exist
f = open('myFile.txt', 'r')
print(f)

text = f.read()
print(text)
f.close() # we should use close()

# write(w) - open a file for writing only and creates a file if file does not exist
# w - create a file
f = open('myFile2.txt', 'w')
print(f)

text = f.read()
print(text)
f.close()

# w - write in exist file
f = open('myFile2.txt', 'w')
f.write("Who are uuuuu")
f.clsoe()

# append(a) - open a file for appending only and creates a file if file does not exist
f = open('myFile2.txt', 'a')
f.write("\nWho are uuuuu")
f.close()

# with statement - to automatically close file after you done with it
with open('myFile2.txt', 'a') as f:
    f.write("\nHey I am inside with")

# create(x) - create a file and gives an error if file does not exist