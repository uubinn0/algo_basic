import copy
from copy import deepcopy

T = int(input())

dyx = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def search_top(arr):
    height = 0

    # 가장 높은 봉우리 값 찾기
    for line in arr:
        for h in line:
            height = max(height, h)

    top_point = []
    # 가장 높은 봉우리 좌표 찾기
    for i in range(map_size):
        for j in range(map_size):
            if arr[i][j] == height:
                top_point.append((i,j))

    return top_point


def dfs(current_point, length, board):
    global max_length
    global chance
    global visited

    current_y, current_x = current_point
    visited[current_y][current_x] = True

    for y, x in dyx:
        new_y, new_x = current_y + y, current_x + x

        # 좌표 밖인 경우 다음 좌표로 넘어간다.
        if new_y < 0 or new_x < 0 or new_y >= map_size or new_x >= map_size: continue

        # 이동 가능 범위인 경우 기존 높이보다 높은 곳인 경우
        if board[new_y][new_x] >= board[current_y][current_x]:
            # 높이를 깎아도 현재 높이보다 높거나 깎았을 때 높이가 낮더라도 찬스가 없는 경우
            if board[new_y][new_x] - cut_height >= board[current_y][current_x] or not chance: continue

            # 찬스가 남아 있고 높이를 깎을 수 있다면
            # 찬스를 쓰고 해당 보드의 좌표 값을 바꿔줘야 한다.
            # 길의 길이를 늘려주고 다음 좌표에 대해서 다시 이를 반복한다.

            # 방문하지 않은 경우만
            if not visited[new_y][new_x]:
                chance = False
                temp_board = copy.deepcopy(board)
                temp_board[new_y][new_x] = temp_board[current_y][current_x]-1
                dfs((new_y,new_x), length+1, temp_board)
                visited[new_y][new_x] = False
                chance = True

        # 이동 가능 범위이면서 기존 높이보다 낮은 경우
        dfs((new_y, new_x), length+1, board)

    max_length = max(max_length, length+1)
    return


for tc in range(1, T+1):
    map_size, cut_height = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(map_size)]
    visited = [[False]* map_size for _ in range(map_size)]
    # print(board)
    # print(visited)
    chance = True   # 공사 가능 여부
    max_length = 0


    # 가장 높은 봉우리 값 찾기
    top_point = search_top(board)
    # print(top_point)

    for start_point in top_point:
        # dfs 멈추는 조건 뭐임?
        dfs(current_point = start_point, length=0, board = board)

    print(max_length)