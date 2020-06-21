# import sys

# n = int(sys.stdin.readline())

# numList = []
# a = list(map(int, sys.stdin.readline().split()))
# # numList.append(a)

# x = int(sys.stdin.readline())
# for i in numList:
#     cnt = 0
#     if x == i:
#         cnt+=1
# print(cnt)

import sys
n = int(sys.stdin.readline())
nList = list(map(int, sys.stdin.readline().split()))
# print(nList)
v = int(sys.stdin.readline())
print(nList.count(v))