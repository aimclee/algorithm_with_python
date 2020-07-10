n = int(input())
grid_list=[]
max_list=[]

#우선 해당되는 값들을 받아온다.
#가로의 합, 세로의 합, 대각선의 합이 필요.
#각각의 합을 비교해서 최대 값을 출력

#1. 값 받아오기
for i in range(n):
    num = list(map(int, input().split()))
    grid_list.append(num)
# print(grid_list)
# print(grid_list[::-1])

'''
1 2 3
4 5 6
7 8 9
'''

#2. 가로의 합 더하기
horizon_tmp_list = []
for j in grid_list:
    horizon_tmp = sum(j)
    horizon_tmp_list.append(horizon_tmp)
else:
    max_list.append(max(horizon_tmp_list))
    # print(max(horizon_tmp_list))

#3. 대각선의 합 더하기
diagonal_rightdown_sum=0
diagonal_leftdown_sum=0

for idx, k in enumerate(grid_list):
    diagonal_rightdown_sum+=grid_list[idx][idx]
else:
    max_list.append(diagonal_rightdown_sum)
    # print(max_list)

for idx, l in enumerate(grid_list[::-1]):
    diagonal_leftdown_sum+=grid_list[::-1][idx][idx]
else:
    max_list.append(diagonal_leftdown_sum)
    # print(max_list)

#4. 세로의 합 더하기

'''
grid_list[0][0]+grid_list[1][0]+grid_list[2][0]
grid_list[0][1]+grid_list[1][1]+grid_list[2][1]
grid_list[0][2]+grid_list[1][2]+grid_list[2][2]
'''

vertical_tmp = 0
second_idx=0
idx=0


while idx < n:
    vertical_tmp += grid_list[idx][second_idx]
    idx+=1
    if idx == n:
        max_list.append(vertical_tmp)
        idx=0
        vertical_tmp=0
        second_idx+=1
    if second_idx==n:
        break
print(max(max_list))
