# for i in range(3):
#     a, b, c, d = map(int, input().split())

# if a+b+c+d == 4:
#     print('E')
# elif a+b+c+d == 3:
#     print('A')
# elif a+b+c+d == 2:
#     print('B')
# elif a+b+c+d == 1:
#     print('C')
# elif a+b+c+d == 0:
#     print('D')

# sum = 0
# for i in range(3):
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# c = list(map(int, input().split()))
# for j in range(4):
#     sum += a[j]
#     if sum == 0:
#         print('D')
#     elif sum == 1:
#         print('C')
#     elif sum == 2:
#         print('B')
#     elif sum == 3:
#         print('A')
#     elif sum == 4:
#         print('E')
# for k in range(4):
#     sum += b[k]
#     if sum == 0:
#         print('D')
#     elif sum == 1:
#         print('C')
#     elif sum == 2:
#         print('B')
#     elif sum == 3:
#         print('A')
#     elif sum == 4:
#         print('E')

# for i in range(4):
#     sum += c[i]
#     if sum == 0:
#         print('D')
#     elif sum == 1:
#         print('C')
#     elif sum == 2:
#         print('B')
#     elif sum == 3:
#         print('A')
#     elif sum == 4:
#         print('E')

# 값을 네개 받아오는 것은 신경쓸 필요 없었음(엔터치기 전까지 안 멈춤)
for i in range(3):
    a = list(map(int, input().split()))
    if a.count(1) == 0:
        print('D')
    elif a.count(1) == 1:
        print('C')
    elif a.count(1) == 2:
        print('B')
    elif a.count(1) == 3:
        print('A')
    elif a.count(1) == 4:
        print('E')
