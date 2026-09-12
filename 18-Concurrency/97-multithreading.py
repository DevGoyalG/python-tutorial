# multithreading in python - it is a technique that allows multiple threads of execution to run concurrently within a single process.
# in py, we can use the threading module to implement multithreading.



import time
# # simple
# # indicates some tasks being done
def func(seconds):
    print(f"Sleep for {seconds} seconds")
    time.sleep(seconds)
    print(f"awake!")

func(4)        # one by one run
func(2)
func(1) 


# by threading
import threading
import time
from concurrent.futures import ThreadPoolExecutor

def func(seconds):
    print(f"Sleep for {seconds} seconds")
    time.sleep(seconds)
    print(f"awake!")

t1 = threading.Thread(target=func, args=[4])
t2 = threading.Thread(target=func, args=[2])
t3 = threading.Thread(target=func, args=[1])

t1.start()      # all in one go run
t2.start()
t3.start()

t1.join()      
t2.join()
t3.join()


# By ThreadPoolExecutor
def poolingDemo():
    with ThreadPoolExecutor(max_workers=1) as executor:
        future1 = executor.submit(func, 4)
        print(future1.result())

        future2 = executor.submit(func, 3)
        print(future2.result())

        future3 = executor.submit(func, 2)
        print(future3.result())

poolingDemo()


# by map func
def poolingDemos():
    with ThreadPoolExecutor(max_workers=1) as executor:
        l = [4,3,2]
        results = executor.map(func, l)

        for result in results:
            print(result)

poolingDemos()