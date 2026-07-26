import queue

q = queue.PriorityQueue()

q.put((2,"hello world ...."))
q.put((4,99))
q.put((3,9.3))
q.put((11,True))
while not q.empty():
    print(q.get()[1])
