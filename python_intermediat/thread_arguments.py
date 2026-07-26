import threading,time

# def print_name(name ,delay):
#     for i in range(3):
#         print(" hello {} !!!".format(name))
#         time.sleep(delay)

# t1 = threading.Thread(target=print_name,args=("shiva",2))
# t2 = threading.Thread(target=print_name,args=("sai",3))

# t1.start()
# t2.start()

def print_table(n):
    for i in range(1,6):
        print('{} X {} = {}'.format(n,i,n*i),end='\n')
        time.sleep(1)

t1 = threading.Thread(target=print_table,args=(2,))
t2 = threading.Thread(target=print_table,args=(5,))
t1.start()
t2.start()

t1.join()
t2.join()
print("hello from main!@!!!")