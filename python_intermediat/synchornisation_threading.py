import threading 
import time 

x = 8192
lock = threading.Lock()

def double():
    global x,lock
    lock.acquire()
    while x < 16384 :
        x *= 2 
        print(x ,end="  ")
        time.sleep(1)
    print("reached to the maximun ")
    lock.release()

def half():
    global x ,lock
    lock.acquire()
    while x > 1 :
        x /= 2 
        print(x ,end="  ")
        time.sleep(1)
    print("minimum value of the thread ")
    lock.release()

t1 = threading.Thread(target=double)
t2 = threading.Thread(target=half)


t2.start()
t1.start()

