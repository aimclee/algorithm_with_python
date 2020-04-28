import statistics as s
import sys
a=[]
for i in range(5):
    n = int(sys.stdin.readline())
    a.append(n)

print(sum(a)//5)
print(s.median(a))
#sort