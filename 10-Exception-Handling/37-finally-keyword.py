# Finally keyword in Python # 

# use of finally : it will not execute always !!

try:
    l = [1, 2, 3, 4]
    i = int(input("Enter the index: "))
    print(l[i])
except:
    print("Some error occured")

finally:
    print("I am always executed")            # this will be print


def func1():
    try:
        l = [1, 2, 3, 4]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Some error occured")
        return 0

    # finally:
        # print("I am always executed")
    print("I am always executed")                # this will not be print

x = func1()
print(x)


def func1():
    try:
        l = [1, 2, 3, 4]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Some error occured")
        return 0

    finally:
        print("I am always executed")               # this will be print
    # print("I am always executed")                

x = func1()
print(x)