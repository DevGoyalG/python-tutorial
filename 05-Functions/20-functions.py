# Functions in Python #

a = 2
b = 8
gmean = (a*b)/(a+b) 
print(gmean)

def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)
a = 2
b = 8
calculateGmean(a,b)

a = 2
b = 8
if(a>b):
    print("First number is greater")
else:
    print("Second number is greater or equal")
calculateGmean(a,b)

def isGreater(a,b):
    if(a>b):
        print("First number is greater")
    else:
        print("Second number is greater or equal")
a = 2
b = 8
isGreater(a,b)

def isLesser(a,b):       # will no error in program
    pass                 # kuch karne ki jarurat nhi hai...mai vapas aauga tum aage chalo