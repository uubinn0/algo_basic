from collections import deque

dyx = [[-1, 0], [0, 1], [1, 0], [0. -1]]

# 상: 0 우: 1 하:2 좌:3
# 파이프에 들어올 수 있는 방향
pipe = {
    1: [0, 1, 2, 3],
    2: [0, 2],
    3: [3, 1],
    4: [0, 1],
    5: [1, 2],
    6: [3, 2],
    7: [3, 0]
}


def search(current_direction, start_point, move_time):
    global visited
    cnt = 0

    cy, cx = start_point
    deq = deque([start_point])
    visited[cy][cx] = True
    
    while deq:
        cy, cx = deq.popleft()

        


T = int(input())

for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    # 현재 방향
    search(-1, (R,C), L)