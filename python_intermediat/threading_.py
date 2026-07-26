# therading :
# A thread is the smallest unit of execution inside a process.

import threading

def function1():
    for x in range(10):
        print("Thread is running")

def function2():
    for x in range(10000):
        print("thread 2 ")

t1 = threading.Thread(target = function1)
t2 = threading.Thread(target=function2)

t1.start()
# t2.start()
t1.join()
print("another text :")