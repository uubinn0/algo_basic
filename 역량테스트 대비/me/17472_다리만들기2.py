from copy import deepcopy
from collections import deque
from collections import defaultdict
from itertools import combinations
from pprint import pprint
import heapq

# 섬 좌표 bfs
def search(y, x):
    global visited

    max_y, max_x = 0, 0
    min_y, min_x = y, x

    deq = deque([(y, x)])

    while deq:
        y, x = deq.popleft()

        max_y = max(max_y, y)
        max_x = max(max_x, x)

        for dy, dx in dyx:
            ny, nx = y + dy, x + dx

            if not (0 <= ny < BOARD_SIZE and 0 <= nx < BOARD_SIZE): continue

            if not visited[ny][nx]: continue

            deq.append((ny, nx))
            visited[ny][nx] = 0

    return (min_y, min_x) , (max_y, max_x)


# 섬 연결 가능 여부 반환
def can_connect_y(a_min_y, a_max_y, b_min_y, b_max_y):
    # y 기준 비교
    # b 섬이 a 섬 범위 안에 있는지 체크
    for by in range(b_min_y, b_max_y+1):
        if a_min_y <= by <= a_max_y: return True
    # a 섬이 b 섬 범위 안에 있는지 체크
    for ay in range(a_min_y, a_max_y+1):
        if b_min_y <= ay <= b_max_y: return True

    return False


def can_connect_x(a_min_x, a_max_x, b_min_x, b_max_x):
    # x 기준 비교
    # b 섬이 a 섬 범위 안에 있는지 체크
    for bx in range(b_min_x, b_max_x+1):
        if a_min_x <= bx <= a_max_x: return True
    # a 섬이 b 섬 범위 안에 있는지 체크
    for ax in range(a_min_x, a_max_x+1):
        if b_min_x <= ax <= b_max_x: return True

    return False


def prim(graph):
    total_cost = 0

    visited = set()
    init_v = 0

    # 최소힙에 초기값 넣기
    min_heap = [[cost, init_v, next_v] for next_v, cost in graph[init_v]]
    heapq.heapify(min_heap)
    visited.add(init_v)

    while min_heap:
        cost, start_v, end_v = heapq.heappop(min_heap)
        if end_v in visited: continue

        visited.add(end_v)
        total_cost += cost

        for adj_v, adj_cost in graph[end_v]:
            if adj_v in visited: continue
            heapq.heappush(min_heap, [adj_cost, end_v, adj_v])

    return visited, total_cost




T = int(input())

for tc in range( 1, T+1):
    BOARD_SIZE = int(input())

    board = [list(map(int, input().split())) for _ in range(BOARD_SIZE)]
    # print(board)
    visited = deepcopy(board)
    dyx = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    island_pos = defaultdict(int)

    # 섬 좌표 찾기
    island_cnt = 0
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            # 섬이라면 bfs 시작해서 좌표 찾기
            if visited[i][j] == 1:
                # print(i, j)
                island_pos[island_cnt] = (search(i, j))
                island_cnt+=1

    # print(island_pos)


    # 섬 간의 거리 구하기
    # 1. 섬끼리의 연결 가능 여부 체크
    # 1-1. 두 섬의 좌표끼리 비교하기. 한 점은 고정하고 다른 한 점이 상대에 들어가는지 체크 어느 한 쪽이라도 들어가면 반대는 무조건
    # 2. 가능한 곳이라면 거리를 구해서 기록
    # 2-1. 거리가 2 이하거나 기존의 값 보다 큰 경우 갱신 안 함


    # 거리를 갱신할 행렬 만들기
    INF = float('inf')
    distance = [[INF] * (island_cnt) for _ in range(island_cnt)]
    # print(distance)

    # 섬 다리 놓기 조합
    # print(island_pos.keys())
    for island_comb in combinations(island_pos.keys(), 2):
        # print(island_comb)
        first_island, second_island = island_comb
        # print(first_island, second_island)
        first_min_y, first_min_x = island_pos[first_island][0]
        first_max_y, first_max_x = island_pos[first_island][1]

        second_min_y, second_min_x = island_pos[second_island][0]
        second_max_y, second_max_x = island_pos[second_island][1]

        # 연결 가능한 섬이면
        # y 범위가 겹침 => 가로로 연결 가능함
        if can_connect_y(first_min_y, first_max_y, second_min_y, second_max_y):
            dis = min(abs(first_max_x - second_min_x), abs(first_min_x - second_max_x))
            distance[first_island][second_island] = min(distance[first_island][second_island], dis - 1)
            distance[second_island][first_island] = min(distance[second_island][first_island], dis - 1)

        # x 범위가 겹침 => 세로로 연결 가능
        if can_connect_x(first_min_x, first_max_x, second_min_x, second_max_x):
            dis = min(abs(first_max_y - second_min_y), abs(first_min_y - second_max_y))
            distance[first_island][second_island] = min(distance[first_island][second_island], dis - 1)
            distance[second_island][first_island] = min(distance[second_island][first_island], dis - 1)

    # pprint(distance)
    # 모든 가능 다리 수
    # 딕셔너리 형태로 저장
    bridge_dict = defaultdict(list)
    total_bridge_cnt = 0
    for i in range(island_cnt):
        for j in range(island_cnt):
            if distance[i][j] != INF:
                bridge_dict[i].append((j, distance[i][j]))
                total_bridge_cnt += 1
    # print(total_bridge_cnt//2)
    # print(bridge_dict)

    v, total_min_cost = prim(bridge_dict)
    if len(v) != island_cnt: total_min_cost = -1

    print(f'#{tc} {total_min_cost}')


# ===========================================================
# def search(y, x, cnt):
#     global board
#
#     deq = deque([(y, x)])
#     board[y][x] = cnt
#
#     while deq:
#         y, x = deq.popleft()
#
#         for dy, dx in dyx:
#             ny, nx = y + dy, x + dx
#
#             if not (0 <= ny < Y and 0 <= nx < X): continue
#
#             if board[ny][nx] != 1: continue
#
#             deq.append((ny, nx))
#             board[ny][nx] = cnt
#             # pprint(board)
#
#     return
#
#
# island_cnt = 10
# for i in range(Y):
#     for j in range(X):
#         # 섬이라면 bfs 시작해서 좌표 찾기
#         if board[i][j] == 1:
#             print(i, j)
#             island_cnt+=1
#             island_pos[island_cnt] = (search(i, j, island_cnt))
#
# pprint(board)
#
# for i in range(Y):
#     for j in range(X):
#         if board[i][j] != 0: