strings = input()

integers=[]
for i in strings:
    if i=='0': integers.append(0)
    elif i=='1': integers.append(1)
    elif i=='2': integers.append(2)
    elif i=='3': integers.append(3)
    elif i=='4': integers.append(4)
    elif i=='5': integers.append(5)
    elif i=='6': integers.append(6)
    elif i=='7': integers.append(7)
    elif i=='8': integers.append(8)
    elif i=='9': integers.append(9)
integers.reverse()

idx=0
sumList=[]
while idx<len(integers):
    sumList.append(integers[idx]*(10**idx))
    idx+=1

n = sum(sumList)
print(n)

yaksu=[]
for j in range(1,n+1):
    if n % j==0:
        yaksu.append(j)
print(len(yaksu))

