# time module - it provides a set of funcs to work with time related operations, such as timekeeping, formatting and time conversions.
# so many funcs :-

# time.time() - func returns the current time as a floating point number
import time
print(time.time())


# time.sleep() - func suspends the execution of the current thread for a specified no. of seconds
print(45)
time.sleep(5)     # in seconds
print("Rohit Sharma")


# time.strftime() - func formats a time value as a string, based on a special format
t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(formatted_time)


# more funcs explored on 
# https://www.w3schools.com/python/ref_module_time.asp