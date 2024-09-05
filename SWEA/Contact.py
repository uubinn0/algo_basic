from collections import defaultdict, deque

T = 10


def bfs(graph, start):
    visited = [False] * (MAX_PEOPLE+1)

    deq = deque([(start,0)]) # 시작 지점 , depth
    visited[start] = True   # 방문 체크
    result = [] # 방문 좌표들 담을 리스트

    while deq:
        v, cnt = deq.popleft()
        result.append((v, cnt))

        for adj in graph[v]:    # 인접한 지점들 확인
            if visited[adj] == False:   # 방문한 적 없으면
                deq.append((adj, cnt+1))
                visited[adj] = True

    return result



for tc in range(1, T+1):
    N, start = map(int, input().split())
    arr = list(map(int, input().split()))
    MAX_PEOPLE = 100

    # 그래프 딕셔너리 만들기
    graph = defaultdict(list)
    # print(graph)
    for i in range(0, len(arr)-1, 2):
        graph[arr[i]].append(arr[i+1])

    # print(graph)

    call_list = bfs(graph, start)

    call_list.sort(key=lambda x:(x[1],x[0]))
    print(call_list)
    result = call_list[-1][0]

    print(f'#{tc} {result}')