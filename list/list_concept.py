import random as r
a = [1, 2, 3, 4, 5]
b = ['a', 'b']
print(b+a)  # 두개의 리스트는 더하기로 합칠 수 있다.

a.insert(1, 8)  # 1번 인덱스에 8을 집어넣는다.
print('insert:', a)

a.pop()  # 제일 뒤에 있는 요소 제거
print(a)

a.pop(2)  # a 리스트 인덱스 2인 값을 제거한다.
print(a)

a.remove(4)  # 4라는 값을 지워라
print(a)

print(a.index(8))  # 8의 인덱스 번호를 출력


b = list(range(1, 11))
print(b)
print(sum(b))  # 리스트의 합 출력
print(max(b))  # 인자 값들 중에서(리스트 내부의) 가장 큰 값 출력
print(min(b))  # 인자 값들 중에서(리스트 내부의) 가장 작은 값 출력
print(min(5, 3, 7))  # 인자 값들 중에서 가장 작은 값 출력

print(b)
r.shuffle(b)  # 무작위로 b 리스트를 섞는다.
print(b)

b.sort()  # (작은 것부터 큰 것 순으로 올라가며) 오름차순으로 정렬
print(b)

b.sort(reverse=True)  # (큰 것부터 작은것 순으로 내려가며) 내림차순으로 정렬
print(b)

b.clear()  # 리스트 내부의 모든 값을 제거하고 빈 리스트로 만든다.
print(b)

c = [23, 12, 36, 53, 19]

for x in enumerate(c):  # '인덱스번호, 해당 값'을 튜플형태로 반환해준다.
    print(x)

print()

for x in enumerate(c):  # '인덱스번호, 해당 값'을 각각 반환해준다.
    print(x[0], x[1])

print()

for index, value in enumerate(c):  # '인덱스번호, 해당 값'을 각각 반환해준다.
    print(index, value)

print()

if all(60 > x for x in c):  # all 함수는 모든 값이 참이어야 해당 조건문이 참이다.
    print('Yes')
else:
    print('No')

if any(15 > x for x in c):  # c 안의 값이 한개라도 참이면 해당 조건문이 참이다.
    print('Yes')
else:
    print('No')

d = [[0]*3 for _ in range(3)]
# 0을 세번 반복해서 리스트로 만들고 이를 리스트로 감싸
# 2차원 리스트로 만든다.
print(d)

for x in d:
    print(x)

for x in d:
    for y in x:
        print(y, end=' ')
    print()
