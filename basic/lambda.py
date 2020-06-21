plus_two = lambda x:x+2
print(plus_two(1))



def plus_one(x):
    return x+1

a = [1,2,3]

#map함수의 앞의 인자에 함수, 뒤의 인자에 값이 들어간다.
#map 함수는 값이 함수에 들어가는 구조다.
print(list(map(plus_one, a)))
print(list(map(lambda x: x+1, a))) 