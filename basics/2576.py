b = []
c = -8
# d = 0

for i in range(7):
    n = int(input())
    if n % 2 == 1:
        b.append(n)
    elif n % 2 ==0:
        c += 1
    # elif n % 2 == 0:
    #     continue
    
    #minNum은 어떻게?
    # for j in b:
    #     if minNum > j:
    #         minNum = j

# for k in b: # b에 저장된 홀수들을 하나씩 어떻게 가져올까?
#     d = d+k

if c == -1:
    print(c)
else:
    print(sum(b))
    print(min(b))
