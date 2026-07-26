'''
What is a daemon thread?

A daemon thread is a background thread that automatically stops when the main program finishes.

Think of it as a helper thread that runs in the background while the main program is doing its work.
'''



import threading ,time 

path = "text.txt"
text = ""

def readfile():
    global path ,text
    while True :  # demon codition end less procressing which is terminated by the main condition not by join .
        with open(path,"r") as f :
            text = f.read()
        time.sleep(3)
def printloop():
    for x in range(30):
        print(text)
        time.sleep(1)

t1 = threading.Thread(target=readfile)
t2 = threading.Thread(target=printloop)
t1.start()
t2.start()