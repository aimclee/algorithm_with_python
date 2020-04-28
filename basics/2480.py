''' 내 풀이 '''
# a, b, c = input().split()

# a = int(a)
# b = int(b)
# c = int(c)

# if 1 <= a <= 6 and 1 <= b <= 6 and 1 <= c <= 6:
#     if a == b == c:
#         print(10000+(a*1000))

#     elif (a == b) != c:
#         print(1000+(a*100))
#     elif (a == c) != b:
#         print(1000+(a*100))
#     elif (b == c) != a:
#         print(1000+(b*100))

#     elif a != b != c:
#         if a > b > c:
#             print(a*100)
#         elif a > c > b:
#             print(a*100)
#         elif b > a > c:
#             print(b*100)
#         elif b > c > a:
#             print(b*100)
#         elif c > a > b:
#             print(c*100)
#         elif c > b > a:
#             print(c*100)

#####################################################

# https://claude-u.tistory.com/223

# 여기에서 map함수로 int클래스의 input().split()이라는 값이 반복문 실행되듯 차례차례 실행되며
# 사용자 입력 값이 a,b,c 변수에 각각 저장된다.

a, b, c = map(int, input().split())

if a == b == c:
    print(10000+a*1000)
elif a == b:
    print(1000+a*100)
elif a == c:
    print(1000+a*100)
elif b == c:
    print(1000+b*100)
else:
    print(100 * max(a, b, c))

# max() -> 제일 큰 값 반환
