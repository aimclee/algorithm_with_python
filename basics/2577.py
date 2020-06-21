# shortcuts
a = int(input())
b = int(input())
c = int(input())

k = a*b*c
k_list = list(str(k))
print(k_list)
for i in range(10):
    k_num_count = k_list.count(str(i))
    print(k_num_count)


################
'''
a = int(input())
b = int(input())
c = int(input())
m = a*b*c
count0 = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0

while True:
    if m == 0:
        break
    elif m % 10 == 0:
        count0 += 1
        m = m // 10
    elif m % 10 == 1:
        count1 += 1
        m = m // 10
    elif m % 10 == 2:
        count2 += 1
        m = m // 10
    elif m % 10 == 3:
        count3 += 1
        m = m // 10
    elif m % 10 == 4:
        count4 += 1
        m = m // 10
    elif m % 10 == 5:
        count5 += 1
        m = m // 10
    elif m % 10 == 6:
        count6 += 1
        m = m // 10
    elif m % 10 == 7:
        count7 += 1
        m = m // 10
    elif m % 10 == 8:
        count8 += 1
        m = m // 10
    elif m % 10 == 9:
        count9 += 1
        m = m // 10

print(count0)
print(count1)
print(count2)
print(count3)
print(count4)
print(count5)
print(count6)
print(count7)
print(count8)
print(count9)
'''
