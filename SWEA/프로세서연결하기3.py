from pprint import pprint
dyx = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def connect(n, connect_cnt, line_len):
    global max_connect, min_line_len

    # 현재 연결한 수 + 남은 코어 수 < 최대 연결 수이면 더 연결할 필요가 없음
    if connect_cnt + len(core_pos) - n < max_connect:
        return

    # 모든 코어에 대해서 연결할지 말지를 선택한 경우
    if n >= len(core_pos):
        # pprint(board)
        # print(line_len)
        # print(min_line_len)
        # 최대 연결 코어 수가 현재 연결 수 보다 작거나
        # 최대 연결 코어 수와 현재 연결 수가 같은데 현재 전선 길이가 작으면
        if (max_connect < connect_cnt) or (max_connect == connect_cnt and min_line_len > line_len):
            max_connect = connect_cnt
            min_line_len = line_len

        return

    # print(core_pos)
    # print(core_pos[n])

    cy, cx = core_pos[n]

    # # 테두리부분의 코어인지 확인
    # # 테두리 부분 코어라면 이미 연결이 된 것이기 때문에 연결 개수 증가 후 다음 코어로 넘어감
    # if cy == 0 or cy == N-1 or cx == 0 or cx == N-1:
    #     connect(n+1, connect_cnt+1, line_len)


    # n번째 코어에 전선 연결을 하지 않을 경우
    connect(n+1, connect_cnt, line_len)

    # n번째 코어에 전선을 연결할 경우
    # 4방향에 대해 전선 연결 경우를 체크
    for dy, dx in dyx:
        ny, nx = cy+dy, cx+dx

        temp_list = []
        # 다른 코어나 전선을 만나기 전까지
        # 범위를 벗어나지 않을 때까지
        # 전선을 놓을 좌표들을 저장
        while (0 <= ny < N) and (0 <= nx < N) and (board[ny][nx] == 0):
            temp_list.append((ny,nx))
            ny, nx = ny+dy, nx+dx

        # 범위를 벗어난게 아닌데 이동을 멈췄다?
        # 장애물을 만났다는 뜻 => 해당 방향으로는 연결할 수 없는 코어
        if 0 <= ny < N and 0 <= nx < N:
            continue

        # 연결을 할 수 있는 코어의 전선 설치 위치가 리스트에 담김
        for temp_y, temp_x in temp_list:
            board[temp_y][temp_x] = 9   # 전선 설치

        connect(n+1, connect_cnt+1, line_len+len(temp_list))

        # 복구
        for temp_y, temp_x in temp_list:
            board[temp_y][temp_x] = 0   # 전선 설치



T = int(input())  

for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    max_connect = 0
    min_line_len = float('inf')

    # 코어 위치 좌표 찾아서 리스트에 저장
    # 테두리에 있는 코어는 이미 연결된 코어이기 때문에
    # 테두리가 아닌 코어만 고려함
    core_pos = []
    for i in range(1, N-1):
        for j in range(1, N-1):
            if board[i][j] == 1:
                core_pos.append((i,j))

    # print(core_pos)
    connect(0,0,0)

    print(f'#{tc} {min_line_len}')