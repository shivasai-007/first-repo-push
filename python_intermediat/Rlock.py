from threading import Thread,Lock,RLock
import time 
# used to over come deadlock conduction 
lock = RLock()

def task2():
    print("tring to accquire the lock \n")
    lock.acquire() # Rlock will run the both the threads... and also behaves like the same lock also at the same time 
    print("the lock of task2 is aqqired \n")
    time.sleep(4)
    lock.release()
    print("thr lock of task2 is relased \n")

def task1():
    print("the thread task1 is aquring the lock \n")
    lock.acquire()
    print("the thread of task1 is quuried the lock \n")
    task2() # loop of processing 
    time.sleep(4)
    lock.release()
    print("the task1 lock is relased ...\n")

def task3():
    print("the thread is acquring the lock ....from task3 \n")
    lock.acquire()
    print("the lock is acquried>>>>\n")
    lock.release()
    print("the lock is relased task3 \n")

t1 = Thread(target=task1)
t2 = Thread(target=task3)
t1.start()
t2.start()
t1.join()
t2.join()