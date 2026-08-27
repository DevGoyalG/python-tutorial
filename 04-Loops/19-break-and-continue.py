# break and continue in Python #


for i in range(12):
    print("5 X", i, "=", 5*(i))

for i in range(12):
    if(i == 10):
        break
    print("5 X", i, "=", 5*(i))

print("Loop ko chor kar nikal gaya")

for i in range(12):
    if(i == 10):
        print("Skip the iteration")
        continue
    print("5 X", i, "=", 5*(i))

# Do While Loop

while True:                      
    print(i)
    i=i+1
    if(i%100==0):
        break