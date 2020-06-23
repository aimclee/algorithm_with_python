n,m = map(int, input().split())
a = [i for i in range(1,n+1)]
b = [i for i in range(1,m+1)]

cnt=[]
for j in a:
    for k in b:
        tmp=j+k
        cnt.append(tmp)
# print(cnt)
# [2, 3, 4, 5, 6, 7, 3, 4, 5, 6, 7, 8, 4, 5, 6, 7, 8, 9, 5, 6, 
# 7, 8, 9, 10]
cntSet = set(cnt)
cntList = list(cnt)
# print(cnt)

#위의 cnt 리스트에서 가장 많이 나온 값을 찾는다.
min=0
answer=[]
for m in cnt:
    x = cnt.count(m)
    if x>min:
        answer.append(x)
        # min=x
# print(answer)

#딕셔너리는 key-value쌍이 똑같으면 한번만 저장된다.
dic = {key:value for key,value in zip(cnt,answer)}
# print(dic)
# for c, d in dic.keys(), dic.values():
#     print(c, d)

answerList=[]
for k,v in dic.items():
    # valueMax = max(dic.keys(),key=lambda k: dic[k])
    valueMax = max(dic.values())
    if v == max(answer):
        answerList.append(k) # value가 4(max)인 key값을 더한다. 
# print(answerList)

for i in answerList:
    print(i, end=" ")
