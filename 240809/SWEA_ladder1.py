import sys
sys.stdin = open('ladder_input.txt', 'r')

T = 10

LADDER_SIZE = 100

dyx = [[-1,0], [0,1], [0,-1]]

def find_start_point():
    for idx, num in enumerate(ladder_board[-1]):
        if num == 2:
            return idx


def find_end_point(y,x):
    global ladder_board

    ladder_board[y][x] = 0

    while y > 0:
        for move_y, move_x in dyx:
            new_y = y + move_y
            new_x = x + move_x
            # print(new_y, new_x)

            # 새로 생성된 좌표가 범위를 벗어나는 경우 다음 새 좌표 생성
            if new_y >= LADDER_SIZE or new_x >= LADDER_SIZE or new_y < 0 or new_x < 0:
                continue

            # 이동할 좌표가 벽인 경우
            if ladder_board[new_y][new_x] == 0:
                continue

            # 이동할 수 있는 경우
            y , x = new_y, new_x
            ladder_board[y][x] = 0

    return x


for _ in range(1, T+1):
    test_case = int(input())

    ladder_board = [list(map(int, input().split())) for _ in range(LADDER_SIZE)]
    # print(ladder_board)

    start_x = find_start_point()
    # print(start_x)

    end_x = find_end_point(y=LADDER_SIZE-1, x=start_x)

    print(f'#{test_case} {end_x}')