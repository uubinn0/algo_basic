from copy import deepcopy
from collections import deque
from collections import defaultdict
from pprint import pprint

Y, X = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(Y)]
# print(board)
dyx = [(-1, 0), (0, 1), (1, 0), (0, -1)]
island_pos = defaultdict(int)


def search(y, x, cnt):
    global board

    deq = deque([(y, x)])
    board[y][x] = cnt

    while deq:
        y, x = deq.popleft()

        for dy, dx in dyx:
            ny, nx = y + dy, x + dx

            if not (0 <= ny < Y and 0 <= nx < X): continue

            if board[ny][nx] != 1: continue

            deq.append((ny, nx))
            board[ny][nx] = cnt
            # pprint(board)

    return


island_cnt = 10
for i in range(Y):
    for j in range(X):
        # 섬이라면 bfs 시작해서 좌표 찾기
        if board[i][j] == 1:
            print(i, j)
            island_cnt+=1
            island_pos[island_cnt] = (search(i, j, island_cnt))

pprint(board)

for i in range(Y):
    for j in range(X):
        if board[i][j] != 0:
            

# ========================================================
# # 섬 좌표 bfs
# def search(y, x):
#     global visited
#
#     max_y, max_x = 0, 0
#     min_y, min_x = y, x
#
#     deq = deque([(y, x)])
#
#     while deq:
#         y, x = deq.popleft()
#
#         max_y = max(max_y, y)
#         max_x = max(max_x, x)
#
#         for dy, dx in dyx:
#             ny, nx = y + dy, x + dx
#
#             if not (0 <= ny < Y and 0 <= nx < X): continue
#
#             if not visited[ny][nx]: continue
#
#             deq.append((ny, nx))
#             visited[ny][nx] = 0
#
#     return (min_y, min_x) , (max_y, max_x)
#
#
# # 섬 좌표 찾기
# island_cnt = 0
# for i in range(Y):
#     for j in range(X):
#         # 섬이라면 bfs 시작해서 좌표 찾기
#         if visited[i][j] == 1:
#             print(i, j)
#             island_cnt+=1
#             island_pos[island_cnt] = (search(i, j))
#
# # print(island_pos)
#
#
# # 섬 다리 설치
# #
# ===========================================================




