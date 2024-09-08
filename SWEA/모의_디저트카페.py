dyx = [(1,1), (1,-1), (-1,-1), (-1,1), (1,1)]

def search(direction_idx, sy, sx, cy, cx, visited):
    global max_len

    # 사각형의 반을 돌고 *2를 했을 때 기존의 최대 값보다 작은 경우
    if direction_idx == 2:
        if len(visited) * 2 <= max_len:
            return

    # 모든 방향에 대해서 모두 회전했다면
    if direction_idx > 3:
        return
    
    # 마지막 방향이면서 시작 지점으로 돌아온 경우 = 사각형을 완성한 경우
    if (direction_idx == 3) and (cy, cx) == (sy, sx):
        max_len = max(max_len, len(visited))
        return

    for c_dirction in range(direction_idx, direction_idx+2):
        dy, dx = dyx[c_dirction]
        ny, nx = cy + dy , cx + dx

        # 새 좌표가 범위를 넘어간 경우
        if ny < 0 or nx < 0 or ny >= N or nx >= N: continue

        # 먹은 적 있는 디저트인 경우
        if board[ny][nx] in visited: continue
        
        visited.add(board[ny][nx])
        search(c_dirction, sy, sx, ny, nx, visited)
        visited.remove(board[ny][nx])



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = set()
    max_len = -1

    for start_y in range(N-2):
        for start_x in range(1, N-1):
            search(0, start_y, start_x, start_y, start_x, visited)

    print(f'#{tc} {max_len}')