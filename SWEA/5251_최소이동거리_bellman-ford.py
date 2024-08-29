T = int(input())


def make_graph(arr, n):
    graph = {i: {} for i in range(n+1)}

    for key, value, weight in arr:
        if key in graph:
            graph[key][value] = weight
    
    return graph


def bellman_ford(start_v):
    # 시작 지점에서 각 정점까지의 최단거리 저장할 리스트 만들기
    short_d = [float('inf') for _ in range(last_v_num+1)]
    short_d[start_v] = 0 # 출발 정점 최단거리 0으로 초기화

    # 정점 수 -1만큼 아래 작업을 반복
    # 인접한 정점까지의 최단경로를 현재 최단거리와 비교하여 작은 값을 저장
    for i in range(last_v_num):
        # 최단거리 갱신이 일어났는지 체크
        update = False

        # 그래프를 돌면서 모든 정점에 대해서 인접한 정점까지의 최단거리 값 비교 및 교체
        for v in graph:
            for adj_v, weight in graph[v].items():
                # 기존 인접정점까지의 거리값 vs 어느 한 정점까지의 거리값 + 어느 한 정점에서 인접정점까지의 거리값
                if short_d != float('inf') and short_d[adj_v] > short_d[v] + weight:
                    short_d[adj_v] = short_d[v] + weight
                    update = True

        # 업데이트가 일어났는지 확인
        # 일어나지 않았을 경우 최단경로를 찾은 것
        if not update:
            break
    
    # 음수 사이클 검사
    for v in graph:
            for adj_v, weight in graph[v].items():
                # 기존 인접정점까지의 거리값 vs 어느 한 정점까지의 거리값 + 어느 한 정점에서 인접정점까지의 거리값
                if short_d != float('inf') and short_d[adj_v] > short_d[v] + weight:
                    # 마지막 검사에서 갱신이 일어난 것은 음수 사이클이 존재하는 것을 의미
                    print('음수 사이클 존재')
                    return -1
    
    return short_d
                

for tc in range(1, T+1):
    last_v_num, edge_cnt = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(edge_cnt)]

    graph = make_graph(arr, last_v_num)
    short_cost = bellman_ford(start_v=0)

    result = short_cost[-1]
    print(f'#{tc} {result}')