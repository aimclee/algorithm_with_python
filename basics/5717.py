import sys

while True:
    M, F = map(int, sys.stdin.readline().split())
    if M ==0 and F==0:
        break
    print(M+F)

# 연산자 and는 그냥 and로 쓰자.
# M & F ==0 보다는 나누어서 쓰자. 