# Recursion in Python #

# find factorial using recursion

# factorial(7) = 7*6*5*4*3*2*1
# factorial(6) = 6*5*4*3*2*1
# factorial(5) = 5*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(1) = 1
# factorial(0) = 1                    # by definition

# factorial(n) = n * factorial(n-1)

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(3))
print(factorial(5))
print(factorial(0))

# for factoorial(5)
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1
# 120

# find fibonacci series using recursion

# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# f(n) = f(n-1) + f(n-2)

# 0 1 1 2 3 5 8 13 21 34 55