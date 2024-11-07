'''
https://www.acmicpc.net/problem/7576

토마토가 퍼져유~~~~
퍼지면 뭐다?
외쳐 BFS
호!
'''

from collections import deque

BOARD_X, BOARD_Y = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(BOARD_Y)]
# print(board)

dyx = [(-1, 0), (0, 1), (1, 0), (0, -1)]

good_tomato = deque()   # 익은 토마토를 담을 큐

# 익은 토마토 찾기
for i in range(BOARD_Y):
    for j in range(BOARD_X):
        if board[i][j] == 1:
            good_tomato.append((i, j, 0)) # 토마토 좌표, 시간

# print(good_tomato)

while good_tomato:
    y, x, time = good_tomato.popleft()

    for dy, dx in dyx:
        ny, nx = y + dy, x + dx

        # 범위 벗어나면 컷
        if not (0 <= ny < BOARD_Y and 0 <= nx < BOARD_X): continue

        # 토마토가 없는 칸이라면 컷
        if board[ny][nx] == -1: continue

        # 이미 익은 토마토면 컷
        if board[ny][nx] == 1: continue

        # 방문처리로 익은 토마토 처리
        board[ny][nx] = 1
        good_tomato.append((ny, nx, time + 1))


board = set(sum(board, []))
# print(set(board))
if 0 in board:
    print(-1)
else:
    print(time)