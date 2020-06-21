a, b = map(int, input().split())

if b > a:
    print(b-a-1)
    for i in range(a+1, b, 1):
        print(i, end=" ")
elif a > b:
    print(a-b-1)
    for i in range(b+1, a, 1):
        print(i, end=" ")
else:
    print(0)
