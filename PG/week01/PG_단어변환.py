'''
https://school.programmers.co.kr/learn/courses/30/lessons/43163

DFS로 풀어보려고 했는데 알파벳을 바꿀 조건을 어떻게 세울지 못 정함...
'''

T = int(input())

for _ in range(1, T+1):
    N = int(input())
    begin, target = map(str,input().split())
    words = list(map(str,input().split()))
    check = [False] * N

    search_word()