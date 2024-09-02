from copy import deepcopy
from collections import deque
from pprint import pprint

T = int(input())

dyx = [[-1,0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1,], [0, -1], [-1, -1]]


def bfs(board, current_position):
    global arr
    click_cnt = 0
    board = deepcopy(board)
    # pprint(board)

    deq = deque([current_position])

    # 각 셀의 인접 폭탄 수로 이중 리스트 초기화
    while deq:
        cy,cx = deq.popleft()

        # 방문하거나 연쇄적으로 숫자 표시가 된 적 없는 좌표인 경우
        if board[cy][cx] == '.':
            board[cy][cx] = 0 # 방문 표시

            # 8방향 탐색
            for y, x in dyx:
                ny, nx = cy+y, cx+x

                # 인접 좌표가 범위를 벗어난 경우 다음 좌표 탐색
                if ny < 0 or nx < 0 or ny >= N or nx >= N: continue

                # 인접 좌표가 폭탄인 경우 현재 좌표에 인근 폭탄 카운트 증가
                if board[ny][nx] == '*':
                    board[cy][cx] +=1

                # 인접 좌표가 폭탄이 아닌 경우 
                # 탐색할 좌표 후보임
                # 다음 탐색을 위해 해당 좌표를 큐에 넣음
                if board[ny][nx] == '.':
                    deq.append((ny,nx))

            # pprint(board)
    # pprint(board)

    zero_q = []

    # 인접 셀 폭탄 수가 0인 셀 클릭 후 주변 셀 열기
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                zero_q.append((i, j))

    zero_q = deque(zero_q)
    # print(zero_q)

    while zero_q:
        cy, cx = zero_q.popleft()

        # 셀 값이 0이지만 이미 열린 값이라면 넘어감
        if arr[cy][cx] != '.' and arr[cy][cx] != '*': continue

        # 폭탄이 아니고 숫자인 경우
        if board[cy][cx] != '*':
            arr[cy][cx] = board[cy][cx] # 주변 폭탄 수를 원본에 적음
            click_cnt += 1

            for y, x in dyx:
                ny, nx = cy + y , cx + x

                # 인접 좌표가 범위를 벗어난 경우 다음 좌표 탐색
                if ny < 0 or nx < 0 or ny >= N or nx >= N: continue

                # 이미 방문한 곳이라면 pass
                if arr[ny][nx] != '.': continue

                # 인접 좌표가 폭탄이 아닌 경우 클릭 없이 열림
                if board[ny][nx] != '*':
                    arr[ny][nx] = board[ny][nx]

    # pprint(board)
    # print(click_cnt)
    return click_cnt
                


for tc in range(1, T+1):
    N = int(input())
    arr = []

    for _ in range(N):
        text = input()
        temp = []
        for str in text:
            temp.append(str)
        arr.append(temp)

    # 폭탄이 아닌 첫 번째 좌표 구하기 함수
    def find_start(arr, N):
        for i in range(N):
            for j in range(N):
                if arr[i][j] != '*':
                    return (i,j)

    start_position = find_start(arr,N)
    # print(start_position)
    click = bfs(arr, start_position)
    # pprint(arr)

    for i in range(N):
        click += arr[i].count('.')

    print(f'#{tc} {click}')