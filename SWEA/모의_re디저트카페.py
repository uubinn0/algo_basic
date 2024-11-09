'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5VwAr6APYDFAWu
'''

T = int(input())
dyx = [(1,1), (1,-1), (-1,-1), (-1,1), (1,1)] # 인덱스 에러 방지용 5개


def search(dir_idx, y, x, START_Y, START_X, visited):
    global max_len

    # 착한 탈출 조건 : 출발 지점과 동일하면 종료
    # 처음 시작 방향이 아니고 시작 지점에 도착했다면 => 아니면 처음 들어와서 걍 나가버림;;
    if (dir_idx == 3) and (y == START_Y and x == START_X):
        # print(visited)
        max_len = max(len(visited), max_len)
        return

    # 나쁜 탈출 조건 2 : 모든 방향을 회전했지만 출발지점에 도착하지 못 한 경우
    if dir_idx > 3:
        return

    # 현재 방향으로 쭉 들어가는 dfs
    # 다음 방향으로 전환하는 dfs
    for cur_dir_idx in range(dir_idx, dir_idx + 2):
        dy, dx = dyx[cur_dir_idx]
        ny, nx = y + dy, x + dx

        # 범위 벗어난 경우
        if not (0 <= ny < N and 0 <= nx < N): continue

        # 이미 방문한 디저트 집이라면
        if board[ny][nx] in visited: continue

        visited.add(board[ny][nx])
        search(cur_dir_idx, ny, nx, START_Y, START_X, visited)
        visited.remove(board[ny][nx])



for i in range(1, 1+T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    max_len = -1

    for start_y in range(N):
        for start_x in range(1, N-1):
            # 출발지점 방문체크 하지 않고 진행
            # 방문 체크 할 경우 마지막에 돌아올 때 방문처리 때문에 시작점으로 돌아오지 못 하게 됨
            search(0, start_y, start_x, start_y, start_x, set())


    print(f'#{i} {max_len}')


