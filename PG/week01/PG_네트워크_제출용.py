'''
https://school.programmers.co.kr/learn/courses/30/lessons/43162
'''

from collections import deque

def solution(n, computers):
    visited = [False] * n   # 방문처리 리스트
    answer = 0
    
    # 리스트를 그래프 형태로
    graph = dict()
    for idx, arr in enumerate(computers):
        graph[idx] = []
        for i in range(len(arr)):
            if i == idx:
                continue
                
            if arr[i] == 1:
                graph[idx].append(i)
    
    def search(idx, visited):        
        deq = deque([idx])
        visited[idx] = True
        
        while deq:
            node = deq.popleft()
            
            for near in graph[node]:
                if not visited[near]:
                    deq.append(near)
                    visited[near] = True
        
        return
    
    for idx in range(len(graph)):        
        # search()를 통해 인접한 노드들의 경우 모두 방문 체크가 된다
        # 따라서 search가 돌아간 횟수가 네트워크의 수가 됨
        # 그래서 아래에 result 증가를 붙여줌
        if not visited[idx]:
            search(idx, visited)
            answer += 1
            
    return answer
        
    