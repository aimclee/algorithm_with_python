n = int(input())
# 소수 = 1과 자기자신을 약수로 가지는 수
prime_number=[]
cnt=0
for i in range(2,n+1):
    for j in range(1,i+1):
        if i%j==0:
            cnt+=1
    if cnt == 2:
        prime_number.append(i)
        cnt=0
    else:
        cnt=0
# print(prime_number)
print(len(prime_number))


