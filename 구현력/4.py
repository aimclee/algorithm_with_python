n = int(input())
scores = list(map(int, input().split()))
a=sum(scores)
#소수점 첫째자리에서 반올림
# 파이썬의 round는 round_half_even 방식을 택한다.
# ex) 4.5 -> 4라는 짝수로 내림되어 출력된다.
# ex) 5.500 -> 6이라는 짝수로 반올림되어 출력된다.
mean = round(a/n)
'''
아래는
4.5가 4라는 짝수로 내림되어 출력되는 것을 
방지하기 위한 코드이다.
a = 67.5
a +=0.5
a=int(a)
print(a)
'''
# print(mean)

# c=[]
min=2147000000 #정수형 크기의 가장 큰 값에 해당됨(2147483647이 정수형 크기의 가장 큰 값)
#인덱스 번호와 해당 값을 같이 쓰고자 할 때, enumerate()를 활용한다.
for idx, x in enumerate(scores):
    deviation = abs(x-mean)
    if deviation < min:
        min=deviation
        score = x # 성적이 높은 학생의 번호를 출력해야 하기 때문에, 성적과 관련된 값도 저장하고 간다.
        res = idx+1
    elif deviation == min: #답이 두개가 되는 경우
        if x > score:
            score = x
            res = idx+1
print(mean, res)
    # c.append(score)
    # if min(scores) == 2:
# dic = {pyeoncha : eachScore for pyeoncha, eachScore in zip(c,scores)}
# print(dic.items())
# print(min(scores))
# print("%d %d" %(mean, dic[]))