cardList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in range(10):
    a,b = map(int, input().split())
    #idx a-1~b-1까지 reverse
    tmp=cardList[a-1:b]
    # tmp.sort(reverse=True)

    del cardList[a-1:b]
    
    #리스트 reverse 필요 없이 a-1번 위치 인덱스 이전에 j를 넣는 것이다.
    for j in tmp:
        cardList.insert(a-1,j)
        
for x in cardList:
    print(x, end=" ")
