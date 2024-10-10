'''
https://www.acmicpc.net/problem/9519

ㅡㅡ 시간초과남
나보고 어쩌라고

글자에 주기가 있음
주기는 짝수일 때와 홀수일 때 다른 것 같음
2, 3은 예외
짝수는 len(txt) -1 의주기마다 반복함
홀수는 len(txt) -2의 주기마다 반복
'''

N = int(input())
txt = input()
cycle = 0
result = ''

# 단어 길이 2, 3 예외처리
if len(txt) ==2:
    print(txt)
    quit()
elif len(txt) == 3:
    if N % 2 == 1:
        result += txt[0]
        result += txt[2]
        result += txt[1]
        print(result)
        quit()


# 짝수 홀수에 따른 사이클 계산
if len(txt) % 2 == 0:
    cycle = len(txt)-1
else:
    cycle = len(txt)-2


def recover_txt(word):
    res = ''

    # 짝수일 때
    if len(txt) % 2 ==0:
        # 갈라진 문자들 붙이기
        for i in range(0, len(word)-1, 2):
            res += word[i]
        # 끼워진 문자들 복구
        for i in range(-1, -len(word), -2):
            res+= word[i]

    else:
        # 갈라진 문자들 붙이기
        for i in range(0, len(word), 2):
            res += word[i]
        # 끼워진 문자들 복구
        for i in range(-2, -len(word), -2):
            res= word[i]

    return res


cnt = N % cycle # 단어 복구 횟수
for _ in range(cnt):
    txt = recover_txt(txt)

print(txt)
