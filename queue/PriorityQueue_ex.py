import queue

data_queue = queue.PriorityQueue()

data_queue.put((1, 'Korea'))
data_queue.put((5,1))
data_queue.put((15,'Vietnam'))
data_queue.qsize()
print(data_queue.get()) # 우선순위가 가장 높은 항목을 얻고 그 값을 제거한다.
print(data_queue.get())


