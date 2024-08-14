from collections import deque
import sys
sys.stdin = open('../input/네트워크.txt', 'r')

T = int(input())




for test_case in range(1, T+1):
    N  = int(input())
    computers = [ list(map(int, input().split())) for _ in range (N)]
    # print(computers)
    visited = [False] * N   # 방문처리 표시용

    # 그래프로 만들기~ 
    # ex. {0: [1], 1: [0], 2: []}
    graph = dict()
    for idx, arr in enumerate(computers):
        graph[idx] = []
        for i in range(len(arr)):
            if i == idx:
                continue
            
            if arr[i] == 1:
                graph[idx].append(i)

    print(graph)

    # 흠... 그래서 뭐 어쩌지? ㅎㅋ

    
    