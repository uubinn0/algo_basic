import sys
sys.stdin = open('s_input.txt')
from collections import defaultdict, deque


# BFS => queue
def bfs(start_vertex):
    # 시작 정점을 큐에 집어넣는다.
    queue = deque([start_vertex])
    visited[start_vertex] = True  # 방문 처리

    while queue:
        vertex = queue.popleft()  # 큐에서 정점 하나 꺼내기
        for v in graph[vertex]:  # 인접한 노드들 방문
            # 조건? 방문한적있는곳은 가면안된다. (무한 방문?)
            if not visited[v]:
                visited[v] = True  # 인접한 정점 방문처리
                queue.append(v)



T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    graph = defaultdict(list)
    for _ in range(M):
        a_vertex, b_vertex = map(int, input().split())
        # 이거 코드 돌아갈까요 ?
        graph[a_vertex].append(b_vertex)
        graph[b_vertex].append(a_vertex)

    group_cnt = 0
    # 모든 정점에 대해서 완전탐색을 진행한다.
    # 그래프를 완탐 => visited (방문처리를 해야한다)
    # 문제에서 사람 번호? 1번부터 시작하니까
    visited = [False] * (N+1)
    for i in range(1, N+1):
        # 모든 정점에 대해서 방문을 하는데
        # 대신, 방문한 적이 없어야한다.
        if not visited[i]:
            # 그래프 완전 탐색 시작!
            bfs(i)
            # dfs()
            group_cnt += 1


    print(f"#{test_case}")
