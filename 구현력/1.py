# import sys
# sys.stdin = open("input.txt", 'rt')

#1. 내풀이
n, k = map(int, input().split(' ')) #n과 k를 차례처례 매핑시킨다.

yaksu = []
for i in range(1, n+1):
    if n%i==0:
        yaksu.append(i)

if k>len(yaksu):
    print(-1)
else:
    print(yaksu[k-1])

#2. 다른 풀이
# for-else 구문 : 
# 여기에서 else문은 for문이 중간에 break 등으로 끊기지 않고 끝까지 수행되었을 때
# 수행하는 코드를 담는다.

n, k = map(int, input().split(' ')) #n과 k를 차례처례 매핑시킨다.
cnt=0
for i in range(1, n+1):
    if n%i==0:
        cnt+=1
    if cnt==k:
        print(i)
        break
else:
    print(-1)