# 문자열과 내장함수

msg = "It is Time"
print(msg.upper())  # 모든 문자열 대문자화
print(msg.lower())  # 모든 문자열 소문자화
print(msg)  # 원래의 값 출력

tmp = msg.upper()
print(tmp)
print(tmp.find('T'))  # tmp에서 문자열 T가 처음으로 나오는 인덱스 번호를 반환
print(tmp.count('T'))  # tmp에서 문자열 T가 몇개 있나
print(msg)
print(len(msg))  # 문자열 전체의 길이

for x in msg:
    print(x, end=' ')

print()

for x in msg:
    if x.isupper():  # x가 대문자면 조건문 참
        print(x, end=' ')

print()

for x in msg:
    if x.islower():  # x가 대문자면 조건문 참
        print(x, end=' ')

print()

for x in msg:
    if x.isalpha():  # x가 알파벳이면 조건문 참
        print(x, end='')

print()

Ascii_upper = 'AZ'
for x in Ascii_upper:
    print(ord(x))  # ord는 아스키넘버를 출력해준다. (참고 : A = 65, Z = 90)

Ascii_lower = 'az'
for x in Ascii_lower:
    print(ord(x))  # a = 97, z = 122

Ascii_num = 65
print(chr(Ascii_num))  # 아스키숫자에 대응하는 문자를 출력
