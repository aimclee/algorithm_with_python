n=int(input())
appletree_list_by_row =[]

#1. 값 받아오기
for i in range(n):
    appletrees = list(map(int, input().split()))
    appletree_list_by_row.append(appletrees)
print(appletree_list_by_row)


#가운데 값을 먼저 더한다.

#수확 : 첫줄, 마지막 줄의 가운데
#n=3, 131 // n=5, 13531 // n = 7, 1357531
#반복문 돌리며 최대 n값하고 같을 때까지 해당 값 출력

#2. 첫줄, 마지막줄 1+3/2,  1+5/2 , 1+7/2

cnt=0
for idx, j in enumerate(appletree_list_by_row):
    print(idx)
    print(j)
    if idx == 0:
        cnt+=j[((n-1)//2)] #첫번째 줄의 가운데 값
        # print(cnt)
        continue
    # print(cnt)
    elif idx == n-1//2:
        '''
        여기에서 오류가 발생하는 것 같다.
        '''
        # for k in j:
        #     cnt+=k
        cnt+=sum(j) # j list에 저장된 모든 값을 더한다.(정가운데줄)
        # print(j)
        # print(cnt)
    elif idx == n-1:
        cnt+=j[((n-1)//2)] # 마지막 줄의 가운데 값
        # print(cnt)
    else:   
        cnt+=j[((n-1)//2)]
        for k in range(1, (idx*2)+1, 1): #k=1~4
            if k == ((n-1)//2):
                break
            cnt=cnt+j[((n-1)//2)-k]
            cnt=cnt+j[((n-1)//2)+k]
    print(cnt)
print(cnt)
