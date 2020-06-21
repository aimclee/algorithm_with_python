n, x = map(int, input().split())
a = list(map(int, input().split()))
# a의 값을 리스트로 받아온다.
# 파이썬 input을 여러번 받아오는데, 몇 개를 받아올 지 모를 때 활용)
for i in range(n):
    # a = input().split()
    if a[i] < x:
        print(a[i], end=" ")
