dyx = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def search(y, x, cur_power):
    global min_power

    # 현재 소요 파워가 기존 파워보다 더 많이 든다면 아웃
    if cur_power > min_power:
        return

    if y == N-1 and x == N-1:
        # print('here')
        min_power = min(min_power, cur_power)
        return

    for dy, dx in dyx:
        ny, nx = y+dy, x+dx

        # 범위 체크
        if not(0 <= ny < N and 0 <= nx < N): continue

        # 방문 체크
        if visited[ny][nx] == True: continue

        # 가려는 곳이 현재와 높이가 같다면
        if board[ny][nx] == board[y][x]:
            visited[ny][nx] = True
            search(ny, nx, cur_power+1)
            visited[ny][nx] = False

        # 가려는 곳이 현재와 높이가 낮다면
        if board[ny][nx] < board[y][x]:
            visited[ny][nx] = True
            search(ny, nx, cur_power)
            visited[ny][nx] = False

        # 가려는 곳이 현재 위치의 높이보다 높다면
        if board[ny][nx] > board[y][x]:
            p = (board[ny][nx] - board[y][x])*2
            visited[ny][nx] = True
            search(ny, nx, cur_power+p)
            visited[ny][nx] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    # print(board)
    min_power = float('inf')

    visited[0][0] = True
    search(0, 0, 0)

    print(f'#{tc} {min_power}')