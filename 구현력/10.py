n = int(input())
chaejum = list(map(int, input().split()))

total_score=0
previous_chaejum=0
previous_jumsu=0

for value in chaejum:
    if (previous_chaejum >=1) and value==1 :
        previous_jumsu+=1
        total_score = total_score+previous_chaejum
    if value == 1:
        total_score+=1
        previous_chaejum+=1
        # if previous_socre >=1:

    elif value == 0:
        total_score+=0
        previous_jumsu=0
        previous_chaejum=0
print(total_score)
    # 이전의 점수가 1이면 누적한다.
    # 전체 점수 & 이전의 점수
    # 누적해서 더하는 경우 : 이전의 점수 + 맞은 경우(1)


