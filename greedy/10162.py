# 그리디: 큰 단위이든 작은 단위이든 값을 쪼개면서 푼다.
import sys

#time//300 -> time // 60 -> time //10-> -1
#Q : 400 // 300 : 100//100 -> 0  

def five_minutes(time):
    push_300 = time // 300
    time = time % 300
    return push_300, time

def one_minute(a,b):
    push_60 = b // 60
    b = b % 60
    return push_60, b

def ten_seconds(c,d):
    push_10 = d // 10
    d = d % 10
    return push_10, d

time = int(sys.stdin.readline())
a,b = five_minutes(time)
c,d = one_minute(a,b)
e,f = ten_seconds(c,d)

if f == 0:
    print(a,c,e, end=" ")
else:
    print(-1)
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)

# print(push_300, push_60, push_10, end=" ")