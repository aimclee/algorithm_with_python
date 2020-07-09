n,m=map(int, input().split())

num_list = list(map(int, input().split()))

cnt=0
tmp=0
for idx, j in enumerate(num_list):
    if j == m:
        cnt+=1
        tmp=0
        continue
    elif j>m:
        tmp=num_list[idx-1]
    else:
        tmp+=j
        if tmp == m:
            cnt+=1
            tmp=j
        elif tmp > m:
            tmp = num_list[idx-1]+num_list[idx]
            if tmp == m:
                cnt+=1
                tmp=j

print(cnt)
# 값을 하나씩 넣어가며 합이 m이되면 cnt+=1하고, cnt=0으로 초기화