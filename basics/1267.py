import sys
n = int(sys.stdin.readline())
m=0

for i in n:
    t = int(sys.stdin.readline().split())
    # Y : 1~29 : 10, 30~59 : 10*2
    # M : 1~59 : 15, 60~119 : 15*2
    if 1<=t<30:
        m+=10