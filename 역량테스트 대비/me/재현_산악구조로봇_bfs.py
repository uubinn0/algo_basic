'''
bfs+메모이제이션?

로봇이 상하좌우 이동
시작 지점은 0,0
도착 지점은 N,N

현 높이보다 높은 높이면 이동할 때 연료 높이차 *2 필요
현 높이와 동일할 경우 연료 1 필요
현 높이보다 낮을 경우 연료 0 필요

N 최대 30
python 6초
'''
from collections import deque
from pprint import pprint
dyx = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def search(sy, sx):
    global visited
    deq = deque([(sy, sx)])
    visited[sy][sx] = 0

    while deq:
        y, x = deq.popleft()

        # 목적지에 도착
        if y == N-1 and x == N-1:
            return

        for dy, dx in dyx:
            ny, nx = y+dy, x+dx

            # 범위 확인
            if not (0 <= ny < N and 0 <= nx < N): continue

            # 현 높이 기준 이동할 곳의 위치의 높이에 따라 다른 처리
            # 높은 곳으로 이동
            if board[y][x] < board[ny][nx]:
                p = (board[ny][nx] - board[y][x]) * 2
            # 동일 높이
            elif board[ny][nx] == board[y][x]:
                p = 1
            # 낮은 높이
            elif board[ny][nx] < board[y][x]:
                p = 0

            # 기존 필요했던 연료량보다 현재 구한 연료량이 적은 경우만 갱신
            if visited[ny][nx] > visited[y][x] + p:
                # 이전까지 쓰인 연료에 추가 필요 연료 더해서 저장
                visited[ny][nx] = visited[y][x] + p
                pprint(visited)
                deq.append((ny, nx))
    return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    INF = float('inf')
    visited = [[INF] * N for _ in range(N)]

    search(0, 0)
    # pprint(visited)
    print(f'#{tc} {visited[N-1][N-1]}')