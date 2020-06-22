t = int(input())
for i in range(1,t+1):
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = a[s-1:e]
    a.sort()
    print("#%d %d" %(i, a[k-1]))


#     for j in range(1,n+1):
#         ns = map(int, input().split()) #여기에서 n개의 정수를 입력받는 방법은?
#     nsList.append(ns)
# print(nsList)
