import queue
#큐 : FIFO
#Queue

data_queue = queue.Queue()
data_queue.put('coding')
data_queue.put('Hello world')

print(data_queue.qsize())
print(data_queue.get())
print(data_queue.qsize())
print(data_queue.get())
print(data_queue.qsize())