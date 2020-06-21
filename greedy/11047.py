#그리디란, 가장 최선의 값을 먼저 계산하면서 답을 풀어나가는 방식
# 큰 단위이든 작은 단위이든 값을 쪼개면서 푼다.
import sys
n, k = sys.stdin.readline().split()
n = int(n)
k = int(k)


values = []
for i in range(n):
    value = int(sys.stdin.readline())
    values.append(value)
values.sort(reverse=True) #values.reverse()
# print(values)  # ->[50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]

# 각각의 값을 하나씩 넣어서 동전개수의 출력값을 구한다.
# k가 4200이면 b=200이 되는데, 이후 어떻게?
# 나머지를 계속 구해서 새로운 값에 저장하고 나온 값을 cnt에 더하면 될거 같다.
# 나머지가 0이 될때까지 나머지 함수를 계속 호출.
# b = k % j (나머지 구하기)


# def share():
cnt = 0
for j in values:
    a = k // j
    b = k % j
    if a == 0:
        continue
    elif a >= 1:
        cnt += a
        if b ==0:
            print(cnt)
            break
        else:
            k=k-(j*a)
            continue
    # share()
            # b//j
            # return cnt



# def remainder(cnt, b):
#     for j in values:
#         c=b//j
#         d=b%j
#         if c == 0:
#             continue
#         elif c >= 1:
#             cnt += c
#             return cnt, d


# cnt = share()
# print(cnt)
# if b == 0:
#     print(cnt)
# else:
#     for i in range(n):
#         cnt, d= remainder(cnt,b)
#     print(cnt)


'''
N, K = map(int, input().split(' '))
val = []
for _ in range(N):
    val.append(int(input()))
val.reverse()

count = 0
for num in val:
    if K%num != K:
        count += K//num
        K = K%num
print(count)
'''