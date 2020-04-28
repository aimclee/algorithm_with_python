import sys
a=[]
b=0
c=[]
for i in range(9):
    n = int(sys.stdin.readline())
    a.append(n)
for j in a:
    b = b+j
    c.append(b)
    if b == 100:
        c.sort()
        break
print(c)