'''
https://school.programmers.co.kr/learn/courses/30/lessons/43163

DFS로 풀어보려고 했는데 알파벳을 바꿀 조건을 어떻게 세울지 못 정함...
DFS에서 BFS로 변경
'''
from collections import deque

import sys
sys.stdin = open('./input/단어변환_input.txt', 'r')


T = int(input())


def search_word(current_word):
    deq = deque([(current_word, 1)])
    check[words.index(current_word)] = True    # 방문 처리

    while deq:
        current_word, cnt = deq.popleft()

        # 다음 단어가 target 단어라면
        if current_word == target:
            return cnt
        
        # 타켓 단어가 아닌 경우
        # 다음 단어 설정해줘야함
        for word in words:
            # current_word와 한 자리만 차이나는 word 찾아서 다음 노드로
            if check_change(current_word, word):
                if not check[words.index(word)]:    # 방문하지 않은 노드일 때만
                    deq.append((word, cnt+1))
                    check[words.index(word)] = True
    
    return 0


# 한 자리만 다른 단어인지 체크
def check_change(current_word, word):
    word_set = set(current_word+word)
    if len(word_set) == 4:
        return True
    else:
        return False



for _ in range(1, T+1):
    N = int(input())    #words 길이
    begin, target = map(str,input().split())
    words = list(map(str,input().split()))
    check = [False] * N

    # target 단어가 단어 리스트에 있는 경우만 서치를 함
    if target in words:
        for word in words:
            # 다음 단어가 현재 단어에서 변형이 가능한 단어인지 확인
            # 한 자리만 차이나는지 확인
            if check_change(begin, word):
                result = search_word(current_word = word)
    else:
        result = 0


    print(result)