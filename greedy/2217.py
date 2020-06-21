# import sys

# n = int(sys.stdin.readline())

# #로프의 개수를 받고, 그것을 반복문을 돌며 제일 작은 거 곱하기 2
# ropes = []

# for i in range(n):
#     rope = int(sys.stdin.readline())
#     ropes.append(rope)
#     ropes.sort(reverse=True) # [10, 15] if input == 10,15
# print(ropes[-1]*n)

N = int(input()) 
rope = [] 
value = [] 
for i in range(N): 
    rope.append(int(input())) 
rope.sort(reverse=True) #1 
for num in range(N): 
    value.append(rope[num]*(num+1)) #2 
print(max(value))
print(rope)
print(value)
# 출처: https://yongku.tistory.com/entry/백준-알고리즘-백준-2217번-로프-파이썬Python [츄르 사려고 코딩하는 집사]
