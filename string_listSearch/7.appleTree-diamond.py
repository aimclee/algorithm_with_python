n=int(input())
appletree_list_by_row =[]

#1. 값 받아오기
for i in range(n):
    appletrees = list(map(int, input().split()))
    appletree_list_by_row.append(appletrees)



#가운데 값을 먼저 더한다.

#수확 : 첫줄, 마지막 줄의 가운데
#n=3, 131 // n=5, 13531 // n = 7, 1357531
#반복문 돌리며 최대 n값하고 같을 때까지 해당 값 출력

#2. 첫줄, 마지막줄 1+3/2,  1+5/2 , 1+7/2

cnt=0
bottom_idx=1
for idx, j in enumerate(appletree_list_by_row):

    if idx == 0:
        cnt+=j[((n-1)//2)] #첫번째 줄의 가운데 값
        continue

    # 가운데줄
    elif idx == ((n-1)//2): 
        # (idx == (n-1)//2): -> 533
        # ((n-1)//2)->533
        # n-1//2 -> 353

        cnt+=sum(j)

    elif idx == n-1:
        cnt+=j[((n-1)//2)] # 마지막 줄의 가운데 값

    else:   
        cnt+=j[((n-1)//2)]

        if idx>((n-1)//2):
            
            for m in range(1, idx-(2*bottom_idx)+1): # -(2*1), -(2*2) ...
                cnt=cnt+j[((n-1)//2)-m]
                cnt=cnt+j[((n-1)//2)+m]
            else:
                bottom_idx+=1

        else:
            for k in range(1,idx+1):
                cnt=cnt+j[((n-1)//2)-k]
                cnt=cnt+j[((n-1)//2)+k]
print(cnt)

