# Exception Handling in Python #

# Simple
a = input("Enter the number : ")
print(f'Multiplication table of {a} is:')

for i in range(1, 11):
    print(f"{int(a)} X {i} = {int(a)*i}")

print("Some lines of code")
print("End of program")

# Exception Handling
a = input("Enter the number : ")
print(f'Multiplication table of {a} is:')

try:
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print("Invalid Input")

print("Some lines of code")
print("End of program")


try:                                             # handle value error
    num = int(input("Enter an integer: "))
    print("Number is integer.")
except ValueError:
    print("Number entered is not an integer.")


try:                                             
    num = int(input("Enter index no.: "))
    a = [2, 8]
    print(a[num])
except ValueError:
    print("Index entered is not an integer.")
except IndexError:
    print("Index Error")