"""
What is multithreading?

Multithreading allows a Python program to run multiple tasks concurrently within the same program.

Think of it like this: one thread can be downloading a file while another thread updates the UI,
and another thread reads data — all seemingly at the same time.

A thread is a smaller unit of a process.

"""
import threading
import time 

# def karthik():
#     for x in range(6):
#         print("varsha!!!!")
#         time.sleep(1)

# t1 = threading.Thread(target=karthik)
# t1.start()
# t1.join()
# print("joe wildcard entery ....")

# def task1():
#     for x in range(5):
#         print("task1 :",x)
#         time.sleep(1)

# def task2():
#     for x in range(5):
#         print("task2 :",x)
#         time.sleep(1)

# t1 = threading.Thread(target=task1)
# t2 = threading.Thread(target=task2)
# t1.start()
# t2.start()

# t1.join()
# t2.join()
# print("program has been ended.....")

