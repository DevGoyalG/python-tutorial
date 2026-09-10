# function caching - optimizes performance by storing the results of expensive or frequent function calls. 
# When the function is called again with the identical arguments, Python bypasses execution and retrieves the saved result instantly.
# Python provides native decorators in the "functools" module to handle this automatically.


from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5

print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")
# below will print fast, because it will fetch the result in cache
print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")