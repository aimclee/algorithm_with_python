import sys
import random
T = int(sys.stdin.readline())
for i in range(T):
    n = int(sys.stdin.readline())
    case = [1,2,3]
    randomNum = random.choice(case)
    # n이 1이거나 2일때 따로 처리를 해줘야한다.
    if n-randomNum > 0:
        pass

    # 1을 한번, 두번, 세번... -> 2를 1번, 2번...->...
    # 1,2,3의 합으로 나타내기.
    # 사고의 전환 : 빼기(빼기를 진행하다가 음수가 나오면 무효처리)
    # 무작위로 뽑기
