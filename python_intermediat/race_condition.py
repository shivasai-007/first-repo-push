'''
What is a race condition?

A race condition happens when multiple threads access and modify the same variable at the same time.

Because thread execution can be interrupted at any moment, the final result may become incorrect.

Imagine two threads both trying to add money to the same bank account. If they update the balance simultaneously,
one update may overwrite the other.
'''



import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        lock.acquire()
        counter += 1
        lock.release()

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()

t1.join()
t2.join()

print("Counter:", counter)