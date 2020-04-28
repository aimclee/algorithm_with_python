a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a > b > c:
    print(c, b, a, end="")
elif a > c > b:
    print(b, c, a, end="")
elif b > a > c:
    print(c, a, b, end="")
elif b > c > a:
    print(a, c, b, end="")
elif c > a > b:
    print(b, a, c, end="")
elif c > b > a:
    print(a, b, c, end="")
