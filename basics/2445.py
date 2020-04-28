a = int(input())

for i in range(1, a+1):
    print(i*'*' + (a-i)*2*' ' + i*'*')
for j in range(a-1, 0, -1):
    print(j*'*' + (a-j) * 2*' ' + j*'*')
