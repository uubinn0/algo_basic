import sys
sys.stdin = open('광직_input.txt', 'r')

T = int(input())


def select_word(idx, word, voca):
    global cnt
    alpha_set = set()

    # 모든 단어의 선택 여부를 정함
    if idx == N:
        for i in range(len(word)):
            alpha_set.add(word[i])
        
        if len(alpha_set) == 26:
            cnt += 1
        return

    # 해당 인덱스의 단어를 선택한 경우
    select_word(idx+1, word+voca[idx], voca)

    # 해당 인덱스 단어를 선택하지 않은 경우
    select_word(idx+1, word, voca)

for test_case in range(1, T+1):
    N = int(input())
    words = [input().strip() for _ in range(N)]
    # print(words)
    cnt = 0

    select_word(idx=0, word='', voca=words)

    print(f'#{test_case} {cnt}')