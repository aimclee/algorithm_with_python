import sys

n = int(sys.stdin.readline())

stackList = []

for _ in range(n):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        stackList.append(order[1])
    elif order[0] == 'pop':
        if len(stackList)>0: print(stackList.pop(-1))
        else: print(-1)
    elif order[0] == 'size':
        print(len(stackList))
    elif order[0] == 'empty':
        if len(stackList) == 0: print(1)
        else: print(0)
    elif order[0] == 'top':
        if len(stackList)>0: print(stackList[-1])
        else: print(-1)

