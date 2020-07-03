n = int(input())
#회문 : 앞뒤가 순서대로 똑같음, 대소문자 구별 안함
#반복문 돌려가며 문자열 계속 검사하기
#3자 -> 0번 == 2번(-1번)
#5자 -> 0번 == 4번(-1번), 1번 == 3번(-2번) 
#7자 -> 0번 == 6번(-1번), 1번 == 5번(-2번), 2번 == 4번(-3번)

string_list = []
char_list = []
for i in range(n):
    string = list(map(str, input())) #map으로 문자열을 한글자씩 구분해서 리스트로 저장됨.

    # string에 저장된 값들을 소문자로 바꾼후 다시 리스트에 저장, 그리고 리스트로 다시 묶어준다.
    # 레퍼런스 : https://www.it-swarm.dev/ko/python/문자열이있는-파이썬-목록을-모두-소문자-또는-대문자로-변환하십시오/968554344/

    string_list.append([x.lower() for x in string]) 
    # string_list.append(string) # [['L', 'e', 'v', 'e', 'l'], ['a', 'b', 'c', 'b', 'a']]
# print(string_list)

cnt=0
for char in string_list:
    for j in range(len(char)//2):
        
        if char[j] == char[-(j+1)]:
            cnt+=1
    else:
        if cnt==(len(char) // 2):
            print('#%d YES' % (i+1))
            cnt=0
        else:
            # 하나의 문자열 포매팅은 하나의 합쳐진 문자열에서 가능
            # print('#%d', 'NO' % (i+1))
            print('#%d NO' % (i+1))
            cnt=0

    #     for j in char:
    #         char_list.append(j)
        
    # for idx, char in enumerate(string_list):
    #     for j in char:
    #         char_list.append(j)
        # string_list.append(char)
# print(string_list)
# print(char_list)