n=int(input())
natural_number = list(map(int, input().split()))
reverseList=[]

def reverse(x):
    hap=0
    for i in str(x):
        reverseList.append(int(i))
    # reverseList.sort(reverse=True)
    # print(reverseList) # [3, 2]
    for idx, v in enumerate(reverseList):
        # print(idx,v)
        hap+=v*(10**idx)
    # for j in reverseList:
    #     for k in range(len(reverseList)):
    #         hap+=j*(10**k)
    return hap

AfterPrimeList = []
def isPrime(x):
    # 소수 : 1과 자기 자신만을 약수로 갖는 수
    
    for i in x:
        cnt=0 #초기화 하는 변수! 반복문 안에 안써줘서 이거때메 엄청 헤맴;;
        for j in range(1,i+1):
            if i%j==0:
                cnt+=1
        if cnt==2:
            AfterPrimeList.append(i)
        
    # print(AfterPrimeList)
    for k in AfterPrimeList:
        print(k, end=" ")
    

BeforePrimeList=[]
for i in natural_number:
    hap = reverse(i)
    BeforePrimeList.append(hap)
    hap=0
    reverseList.clear()
# print(BeforePrimeList)

isPrime(BeforePrimeList)