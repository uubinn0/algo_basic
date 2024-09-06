'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4suNtaXFEDFAUf

프로세서의 연결을 선택할지 말지를 결정하는 dfs
해당 프로세서의 연결을 선택한 경우 연결될 수 있는 방향으로 이어주기
'''

import time

st_t = time.time()

dyx = [[-1, 0], [0, 1], [1, 0], [0, -1]]

# 프로세서 좌표 찾기
def find_processer(board):
    arr = []

    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                arr.append((i,j))

    return arr


def connect(board, idx, connect_cnt, line_len):
    global result

    result.sort(key=lambda x:(x[0], -x[1]))

    # 현재 연결된 프로세서에 남은 프로세서를 모두 더해도 기존 최대 연결 값보다 작은 경우 더하지 않음
    if result:
        if connect_cnt + (N-idx) < result[-1][0]: return

    # 종료 조건
    # 결과 값에 연결된 프로세서 수, 전선 길이 저장
    if idx >= len(processer_yx):
        result.append((connect_cnt, line_len))
        return
    
    # 해당 프로세서의 전선을 연결하지 않을 경우
    connect(board, idx+1, connect_cnt, line_len)


    # 해당 프로세서에 전선을 연결할 거임
    cy, cx = processer_yx[idx]

    # 해당 좌표가 테두리 근처라 연결이 이미 되어있는 상태라면
    # 연결 카운트를 늘리고 다음 인덱스로 넘어감
    if cy == 0 or cx == 0 or cy == N-1 or cx == N-1:
        connect(board, idx+1, connect_cnt+1, line_len)
    
    # 연결이 안 된 프로세서
    # 4방향을 보며 벽/전선/프로세서를 만날 때까지 수를 센다.
    for dy, dx in dyx:
        ny, nx = cy+dy, cx+dx

        line_pos_list = []  # 전선을 깐 좌표 리스트

        # 벽에 닿기 전까지 or 전선(9)을 만날 때까지 or 프로세서(1)을 만날 때까지 계속 한 방향으로 이동
        while (0 <= ny < N) and (0 <= nx < N) and (board[ny][nx] == 0):
            line_pos_list.append((ny,nx))
            ny, nx = ny+dy, nx+dx   # 같은 방향으로 이동

        # 마지막에 멈춘 좌표가 벽 옆이 아니라면 연결을 하지 못했다는 의미
        if (0 <= ny < N) and (0 <= nx < N): continue

        # 벽에 도착했음 = 연결 가능
        for temp_y, temp_x in line_pos_list:
            board[temp_y][temp_x] = 9   # 전선 설치

        connect(board, idx+1, connect_cnt+1, line_len+len(line_pos_list))

        # 복구
        for temp_y, temp_x in line_pos_list:
            board[temp_y][temp_x] = 0   # 전선 설치 제거

        


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    result = []

    processer_yx = find_processer(board)
    # print(processer_yx)

    # 종료 조건: 모든 프로세서의 연결 유무를 결정한 경우
    # 누적값: 전선 길이, 연결된 프로세서 수
    connect(board, 0, 0, 0)

    result.sort(key=lambda x:(x[0], -x[1]))

    print(f'#{tc} {result[-1][1]}')

    print(time.time() - st_t)