'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4suNtaXFEDFAUf

1. 각 프로세서 좌표를 찾기
2. 연결이 필요한 프로세서인지 확인 => 연결이 이미 된 경우 패스
    x좌표가 0 또는 N 혹은 y좌표가 0 또는 N인 경우 이미 연결됨
3. 연결이 필요한 프로세서의 경우 상우하좌를 순회하며 연결할 수 있는 경로를 찾는다
    각 프로세서를 어느 방향으로 전선을 연결할 지 결정한다.
4. 전선을 이어본다.
    전선이 벽에 닿는지 확인한다.
    연결이 된 경우 연결된 수 +1 길이 + 해준다
5. 모든 프로세서에 대해 연결 여부가 결정되면 (연결된 수, 길이)를 result 리스트에 저장한다.

'''
dyx = [[-1, 0], [0, 1], [1, 0], [0, -1]]


# 프로세서 좌표 찾기
def find_processer(board):
    arr = []

    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                arr.append((i,j))

    return arr


def connect(process_pos, idx):
    global result
    connect_cnt = 0
    line_len = 0


    # 모든 프로세스를 모두 선택 했다면
    if idx >= N:
        result.append((connect_cnt, line_len))


    for position in process_pos:
        # 현재 좌표
        cy, cx = position

        # 4방향을 보면서 갈 수 있는 방향인지 체크
        for dy, dx in dyx:
            ny, nx = cy+dy, cx+dx

            # 벽이라면 = 연결이 이미 됨
            if ny < 0 or nx < 0 or ny >= N or nx >= N:
                connect_cnt += 1
                break

            # 프로세서가 이미 있는 좌표라면
            if board[ny][nx] == 1: continue

            # 전선이 깔린 좌표라면
            if board[ny][nx] == 9:


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    result = []

    processer_pos = find_processer(board)

    connect(processer_pos, 0)