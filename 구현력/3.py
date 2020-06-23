# import random -> random함수 실패
n,k = map(int,input().split())
value = list(map(int, input().split()))
# print(value)
# hap = [random.choice(value) for i in range(1,n+1) for j in range(3)]

hap =set()
# 리스트는 아래와 같은 방법으로 추출해올 수 없다.
# for i in range(n-k+1):
#     for j,m,l in value[i], value[i+1], value[i+2]: #value[i:i+3]을 추출해온다.
#         hap.append(j+m+l)

# 리스트의 append()가 있듯, set에서는 add()가 있다.
# 차이점은 전자는 값의 중복을 허용하지만, 후자는 허용하지 않는다.
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            hap.add(value[i]+value[j]+value[m])
# print(hap)  
hap = list(hap)
hap.sort(reverse=True)
# print(hap)
print(hap[k-1])
