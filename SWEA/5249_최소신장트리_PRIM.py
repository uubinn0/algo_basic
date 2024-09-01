'''
시작 정점의 인접한 정점 중 가중치가 가장 작은 정점과의 간선을 선택하는 알고리즘

POINT ! 우선순위 큐를 사용한다.

1. 시작 정점 선택
2. 정점과 인접한 정점들을 우선순위 큐에 삽입
3. 가중치가 가장 작은 정점이 방문하지 않은 정점인 경우 간선을 신장 트리에 추가
'''
import heapq

def make_graph(arr):
    graph = {i : {} for i in range(V+1)}

    for start_v, end_v, weight in arr:
        graph[start_v][end_v] = weight
        graph[end_v][start_v] = weight
    
    return graph


def prim(graph, init_v):
    print(graph)

    cost = 0
    visited  = set()
    visited.add(init_v) # 방문처리

    min_heap = []
    for end_v, weight in graph[init_v].items():
        min_heap.append([weight, end_v])
    
    heapq.heapify(min_heap)

    while min_heap:
        w, e_v = heapq.heappop(min_heap)

        if e_v in visited : continue   # 이미 방문했다면 넘어감

        # print('->', visited)
        if set(visited) == 1:   # 모두 방문했다면 종료
            return cost

        # 방문하지 않은 정점이라면 방문 처리를 하고
        visited.add(e_v)
        # print(visited)
        cost += w   # 가중치 증가

        # 해당 정점과 인접한 정점들 우선순위 큐에 추가
        for end_v, weight in graph[e_v].items():
            if end_v not in visited:
                heapq.heappush(min_heap, [weight, end_v])

    return cost

T = int(input())

for tc in range(1,T+1):
    V, E = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]

    graph = make_graph(arr)
    result = prim(graph, 0)

    print(f'#{tc} {result}')
