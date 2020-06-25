n=int(input())
k=list(map(int, input().split()))

def digit_sum(x):
    return sum(x)

place_value=[]
sumList=[]
for i in k: #i=125
    for j in range(8):
        remainder = i%10 # r=5 // 2 // 1
        divisor = i//10 # d = 12 // 1 // 0
        place_value.append(remainder) # [5, 2, 1]
        if divisor > 0:
            i=i//10
            continue # 두번째 반복문이 continue된다.
        else:
            break # 두번째 반복문만 break된다.
    s = digit_sum(place_value)
    sumList.append(s)
    place_value.clear()
dic = {key:value for key,value in zip(sumList,k)}
print(sumList)
print(dic.get(max(sumList)))


'''
import sys
# sys.stdin=open("input.txt", "r")
def digit_sum(x):
    sum=0
    while x>0:
        sum+=x%10
        x=x//10
    return sum

##############################################################
정수를 문자열화 시키고 다시 정수화 시켜서 자릿수를 가져올 수 있다.
def digit_sum(x):
    sum=0
    for i in str(x): 
        sum+=int(i)
    return sum
##############################################################

n=int(input())
a=list(map(int, input().split()))
res=0
max=-2147000000
for x in a:
    tot=digit_sum(x)
    if tot>max:
        max=tot
        res=x
print(res)
'''