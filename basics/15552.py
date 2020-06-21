from sys import stdin
# import sys
# import sys의 경우, sys.stdin.readline() 이라고 작성해줘야 한다.

t = int(input())

for i in range(t):
    a, b = map(int, stdin.readline().split())
    print(a+b)
