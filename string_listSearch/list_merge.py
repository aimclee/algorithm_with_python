n=int(input())
a = list(map(int,input().split()))

m=int(input())
b = list(map(int, input().split()))

merged=[]
for i in a:
    merged.append(i)
for j in b:
    merged.append(j)
merged.sort()

for k in merged:
    print(k, end=' ')