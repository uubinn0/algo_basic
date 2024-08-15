'''
https://school.programmers.co.kr/learn/courses/30/lessons/43162
'''

from collections import deque
import sys
sys.stdin = open('./input/네트워크.txt', 'r')

T = int(input())


def search(idx):
    global visited

    deq = deque([idx]) # 시작노드 큐 추가
    visited[idx] = True # 시작노드 방문 처리

    while deq:
        node = deq.popleft()
        for near in graph[node]:    # node의 인접노드 방문여부 파악
            if not visited[near]:   # 인접노드를 방문하지 않았다면
                deq.append(near)    # 인접노드 큐에 추가
                visited[near] = True    # 방문함 처리

    return



for test_case in range(1, T+1):
    N  = int(input())
    computers = [ list(map(int, input().split())) for _ in range (N)]
    # print(computers)
    visited = [False] * N   # 방문처리 표시용
    result = 0  # 네트워크 수

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

    # print(graph)

    # 흠... 그래서 뭐 어쩌지? ㅎㅋ
    # 인접이니까 bfs로 할까
    # 네트워크 수 == 순환하는 그래프 수?
    # 순환체크는 어떻게 하지

    for idx in range(len(graph)):
        # search()를 통해 인접한 노드들의 경우 모두 방문 체크가 된다
        # 따라서 search가 돌아간 횟수가 네트워크의 수가 됨
        # 그래서 아래에 result 증가를 붙여줌
        if not visited[idx]:
            search(idx)
            result += 1

    print(f'#{test_case} {result}')
    
    
    