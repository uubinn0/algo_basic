import heapq

T = int(input())


def make_graph(arr, n):
    graph = {i: {} for i in range(n + 1)}

    for key, value, weight in arr:
        if key not in graph.keys():
            graph[key] = {value: weight}
        else:
            graph[key][value] = weight

    return graph


def dijkstra(start_v):
    # 최단 거리 리스트 만들기
    short_d = [float('inf') for _ in range(last_node_num+1)]
    # 시작점 최단거리 0으로 초기화
    short_d[start_v] = 0
    # print(short_d)

    # 최소힙에 시작지점과 시작지점까지의 거리 넣어주기
    min_heap = [[short_d[start_v], start_v]]
    heapq.heapify(min_heap)

    while min_heap:
        # 우선순위에서 가장 작은 값을 꺼냄
        current_d, current_v = heapq.heappop(min_heap)
        # print('->', current_d, current_v)

        if short_d[current_v] < current_d: continue

        # 해당 노드와 인접한 점들을 순회함
        # print(graph[current_v].items())
        for adj_v, weight in graph[current_v].items():
            # 현재 노드까지의 거리 값 + 인접 노드까지의 가중치 < 기존 인접 노드의 값
            if current_d + weight < short_d[adj_v]:
                short_d[adj_v] = current_d + weight
                # 잊지말자 바뀐 weight 값을 큐에 넣어줘야 함
                heapq.heappush(min_heap, [short_d[adj_v], adj_v])

    return short_d


for tc in range(1, T+1):
    last_node_num, edge_cnt = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(edge_cnt)]
    # print(arr)

    graph = make_graph(arr, last_node_num)
    # print(graph)
    short_path = dijkstra(start_v=0)
    result = short_path[-1]

    print(f'#{tc} {result}')

