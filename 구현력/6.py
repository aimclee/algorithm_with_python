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
            continue
        else:
            break
    s = digit_sum(place_value)
    sumList.append(s)
    place_value.clear()
dic = {key:value for key,value in zip(sumList,k)}
print(sumList)
print(dic.get(max(sumList)))