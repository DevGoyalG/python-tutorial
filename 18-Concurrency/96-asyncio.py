# AsyncIO - ia a programming pattern that allows for high performance I/O operations in a concurrent and non-blocking manner. 
# In python, async programming is achieved through the use of "asyncio" module and asynchronous func.

# simple
# import time

# def function1():
#     time.sleep(3)
#     print("func 1")

# def function2():
#     time.sleep(3)
#     print("func 2")

# def function3():
#     time.sleep(3)
#     print("func 3")

# function1()
# function2()
# function3()

# asyncio
import time
import asyncio

async def function1():
    # await asyncio.sleep(1)
    print("func 1")

async def function2():
    # await asyncio.sleep(2)
    print("func 2")

async def function3():
    # await asyncio.sleep(3)
    print("func 3")

async def main():
    # await function1()
    # await function2()
    # await function3()

    # or for print

    L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )

    print(L)

asyncio.run(main())
