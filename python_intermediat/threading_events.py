"""
What is an Event?

An Event is a synchronization object that allows one thread to signal another thread.

You can think of it like a traffic signal:

One thread waits at the red light.

Another thread changes the light to green.

Then the waiting thread continues its work.

Python provides this through 'threading.Event'.
"""


import threading,time

event = threading.Event()

# def myfunc():
#     print("wating for the event to triggered!!!")
#     event.wait()
#     print("the thread got the access to work")

# t1 = threading.Thread(target=myfunc)
# t1.start()
# x = input("do you want to give access to the thread (Y/N):")

# if x.lower() == "y" :
#     event.set()
'''-----------------------------------------------------------------'''
# def wating():
#     print("the thread is wating for the access \n")
#     event.wait()
#     print("the thread got accessed \n")

# def setting():
#     print("an I/O operation is going on and wating to complite \n")
#     time.sleep(5)
#     event.set()
#     print("the io operation is done the thread got access ..\n")

# t1 = threading.Thread(target=wating)
# t2 = threading.Thread(target=setting)

# t1.start()
# t2.start()

# t1.join()
# t2.join()
'''-----------------------------------------------------------------'''
def student():
    print('student is wating to write the exam ')
    event.wait()
    print("Exam started, writing now!")
def teacher():
    print('the exam will be started in 2 mins ')
    time.sleep(2)
    event.set()
    print("start the exam!!!!")

t1 = threading.Thread(target=student)
t2 = threading.Thread(target=teacher)


t1.start()
t2.start()

t1.join()
t2.join()