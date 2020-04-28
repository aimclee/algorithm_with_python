import sys
n = int(sys.stdin.readline())
time = []
startTime=[]
endTime=[]
num = []
cnt = 0

#입력된 값을 받고 리스트에 더하는 작업
for i in range(0,n):
    start, end = map(int, sys.stdin.readline().split())
    startTime.append(start)
    endTime.append(end)
    time.append([start,end])
    time.sort()

# print(time) # [[0, 6], [1, 4], [2, 13], [3, 5], [3, 8], [5, 7], [5, 9], [6, 10], [8, 11], [8, 12], [12, 14]]
# first_start = time[0][0]
# first_end = time[0][1]
for j in range(0,n):
    start = time[j][0]
    end = time[j][1]
    for f, s in time:
        if start == f:
            break
        elif start<f & end<=s:
            cnt+=1
        num.append(cnt)
num.sort(reverse=True)
print(num)

# for j in range(0,n):
#     start = time[n][n]
#     end = time[n][n+1]


        
    # for f, s in j[0], j[1]:-> 2차원 배열의 경우에도 반복문은 일반적으로 생각하자.

            # 새로운 리스트에 더하기.
            # 리스트의 인덱스 + 1의 max값 출력
 

#sort를 통해 시작시간이 제일 작은 것이 제일 앞으로 와야 한다.
#딕셔너리 안에다가 튜플/리스트를 넣는다



# meeting = list(first_start, first_end)



# print(zipped)
# print(zipped[0][1])

# 제일작은 숫자를 찾으면 그 부분만 딕셔너리로 바꾼다.
# 1. 반복문을 돌리면서 앞의 숫자는 제일 작은 숫자를 먼저 찾는다
# 2. 찾은 제일 작은 숫자의 끝나는 시간을 찾는다.
# 3. 그 다음 제일 작은 시작시간을 찾는다.
# 4. 만약 3에서 찾은 숫자가 1과 2사이의 범위에 있는 숫자라면, 그 경우는 건너뛴다.
# 5. 이렇게 중복을 제외한 시작과 끝값들의 개수를 저장해둔다. 
# 6. 한바퀴 돌고 나서, 1에서 찾은 숫자 그 다음 작은 숫자를 찾는다.
# 7. 1부터의 과정을 반복한 후, 마지막에 가장 큰 회의의 개수의 값을 출력한다.

# for s,e in zip(startTime, endTime):
#     print (s,e)
    # endTime.sort()
    # time[startTime[i]] = endTime[i]
    # sorted(time.keys()) # https://rfriend.tistory.com/473(딕셔너리의 키값을 기준으로 오름차순 정렬)
# print(t)
# print(set(startTime)) #리스트는 값의 중복을 허용한다.
# print(set(endTime))
# print(time)
# print(sorted(time.keys()))
# print(reservation)
# zipped = list(zip(startTime,endTime))
# print(zipped.sort())

