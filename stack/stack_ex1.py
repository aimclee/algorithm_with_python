# 프로세스 스택
# : 운영체제 과목에서 다루어지는 스택이다.
# 쉽게 생각해서 함수가 재귀함수 형태라면 반복해서 호출되는데,
# 스택처럼 함수 위의 함수가 차례대로 쌓이다가 실행이 종료되면 
# 함수가 제일 마지막에 실행된 함수부터 사라지는 구조를 가진다.

# 재귀 함수
# 4 -> 3-> 2-> 1-> 0-> -1(ended) -> 0 -> 1 -> 2 -> 3 -> 4
def recursive(data):
    if data < 0:
        print ("ended")
    else:
        print(data)
        recursive(data - 1)
        print("returned", data)

recursive(4)