# import queue
import sys

n = int(sys.stdin.readline())
# q = queue.Queue()
queueList = []
for _ in range(n):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        queueList.append(order[1])
        # q.put(int(order[1]))
    elif order[0] == 'front':
        if queueList: print(queueList[0])
        else: print(-1)
    elif order[0] == 'back':
        if queueList: print(queueList[-1])
        else: print(-1)
    elif order[0] == 'size':
        # print(q.qsize())
        print(len(queueList))
    elif order[0] == 'empty':
        # print(int(q.empty()))
        if queueList: print(0)
        else: print(1)
    elif order[0] == 'pop':
        if queueList:
            f = queueList[0]
            del queueList[0]
            print(f)
        else:
            print(-1)
        # print(q.get())
        # if q.empty == True:
        #     print(-1)


# 배울 점들

'''
1. 받아온 값들에 대해서 리스트처럼 인덱싱 가능
2. if문이 너무 길어지게 될 때 대처법
'''

