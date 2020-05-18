import sys

# 1,3,5,7,8,10,12월 : 31일
# 4,6,9,11 : 30일
# 2월 : 28일
# 3월 1일~11월 30일 : 60일 ~ 334일

#함수 만들어서 1월부터 x월까지 증가할 때 그 값을 더해가며 진행.
#범위를 지정하고 60일~334일 사이에 있으면, 그 부분은 빼고 진행.
n = int(sys.stdin.readline())
date = []
for _ in range(n):
    date.append(list(map(int, sys.stdin.readline().split())))

# x[0]을 기준으로 정렬
date = sorted(date, key= lambda x : [x[0], x[1], x[2], x[3]])
print(date)
month = [1,32,60,91,121,152,182,213,243,273,304,334]

for sm, sd, em, ed in date:





#일단 월부터 계산, 그리고 일을 계산
#월이 3월부터 연결이 안되면, 0을 출력. 그리고 일 파악 

#월과 일을 연관시킨다.
#리스트, 반복문
