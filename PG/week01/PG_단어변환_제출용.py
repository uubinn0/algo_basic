'''
https://school.programmers.co.kr/learn/courses/30/lessons/43163

DFS로 풀어보려고 했는데 알파벳을 바꿀 조건을 어떻게 세울지 못 정함...
DFS에서 BFS로 변경
'''
from collections import deque

def solution(begin, target, words):
    result = 0
    check = [False] * len(words)
    
    def check_change(current_word, word):
        word_set = set(current_word+word)
        if len(word_set) == len(word)+1:
            return True
        else:
            return False
        
        
    def search_word(current_word, check):
        deq = deque([(current_word, 1)])
        check[words.index(current_word)] = True
        
        while deq:
            current_word, cnt = deq.popleft()
            
            if current_word == target:
                return cnt
            
            for word in words:
                if check_change(current_word, word):
                    if not check[words.index(word)]:
                        deq.append((word, cnt+1))
                        check[words.index(word)] == True
                        
        return 0
        
    
    
    if target in words:
        for word in words:
            if check_change(begin, word):
                result = search_word(current_word=word, check = check)
    else:
        result = 0
    
    return result