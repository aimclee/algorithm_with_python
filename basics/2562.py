b = []
for i in range(9):
    num = int(input())
    b.append(num)
    if i == 0:
        max_num = b[0]
        continue
    elif i>=1:
        # max_num과 비교해야할거 같은데...
        if max_num > b[i]:
            continue
        else:
            max_num = b[i]

print(max_num)      
print(b.index(max_num)+1)
