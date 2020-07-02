import sys
# sys.stdin=open("9.txt", "r")

# ! TypeError: 'int' object is not callable -> 변수와 함수가 같을 때 발생하는 오류.
# 따라서, 변수와 함수를 같게 지정하지 않는다!

n = int(input())
answer = []

def all_same(same_dot):
    sum = 10000 + (same_dot*1000)
    return sum
def two_same(same_dot):
    sum = 1000 + (same_dot*100)
    return sum
def diff(max_value):
    sum = max_value*100
    return sum

for i in range(n):
    dotList = list(map(int, input().split()))
    if dotList[0] == dotList[1] == dotList[2]:
        all_same_var = all_same(dotList[0])
        answer.append(all_same_var)
    if dotList[0]==dotList[1]:
        if dotList[0] != dotList[2]:
            two_same_var = two_same(dotList[0])
            answer.append(two_same_var)
    elif dotList[1] == dotList[2]:
        if dotList[1] != dotList[0]:
            two_same_var = two_same(dotList[1])
            answer.append(two_same_var)
    elif dotList[0] == dotList[2]:
        if dotList[0] != dotList[1]:
            two_same_var = two_same(dotList[2])
            answer.append(two_same_var)
    elif dotList[0] != dotList[1] != dotList[2]:
        max_value = max(dotList)
        diff_var = diff(max_value)
        answer.append(diff_var)
print(max(answer))



'''
dot1,dot2,dot3 = map(int, input().split())
if dot1 == dot2 == dot3:
    all_same = all_same(dot1)
for j in range(1,6+1):
    if ((dot1 == dot2) != j) or ((dot2 == dot3) != j) or ((dot1 == dot3) != j):
        two_same = two_same()
'''



    
        