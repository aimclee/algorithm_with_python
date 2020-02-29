import queue
#LifoQueue()->스택하고 똑같다고 생각하면 됨.

data_queue = queue.LifoQueue()
data_queue.put('hello')
data_queue.put('World')
print(data_queue.qsize())
print(data_queue.get())