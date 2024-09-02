from collections import deque

T = int(input())


dyx = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def bfs(deq):
    global visited

    while deq:
        cy, cx = deq.popleft()

        for dy, dx in dyx:
            ny, nx = cy + dy, cx + dx

            # 범위 넘어간 경우 다음 좌표로
            if ny < 0 or nx < 0 or ny >= N or nx >= M: continue

            # 땅이면서 방문한 적 있는 좌표라면
            if board[ny][nx] == 'L' and visited[ny][nx] == 1: continue

            if 



for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[(0,0)] * M for _ in range(N)]   # 방문체크와 최소거리값

    # W 좌표를 담을 데크
    deq = deque()
    
    # W 찾기
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'W':
                deq.append([(i, j)])

    # W 좌표들에 대해서 bfs로 탐색하며 L까지의 최소값 찾음
    bfs(deq)