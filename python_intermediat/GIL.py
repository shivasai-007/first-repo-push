"""
Important concept: GIL

Python has something called the Global Interpreter Lock (GIL).

It means that in CPython, only one thread executes Python bytecode at a time.

So:

Multithreading is excellent for I/O-bound tasks

It is not ideal for CPU-bound tasks (heavy calculations)

For CPU-bound tasks, Python’s multiprocessing module is often better.
"""

import threading
import time 

def print_letter():
    for i in range(ord("A"),ord("E")+1):
        print(chr(i),end=" ")
        time.sleep(1)

def print_num():
    for x in range(1,6):
        print(x)
        time.sleep(1)

t1 = threading.Thread(target=print_letter)
t2 = threading.Thread(target=print_num)

t1.start()
t2.start()

t1.join()
t2.join()
print("helli form main")

