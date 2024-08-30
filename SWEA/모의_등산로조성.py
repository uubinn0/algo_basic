from copy import deepcopy
from pprint import pprint

T = int(input())


dyx = [[-1, 0], [0, 1], [1, 0], [0, -1]]


# 최고점 좌표를 찾는 함수
def top_point(arr):
    top_num = 0

    for i in range(map_size):
        for j in range(map_size):
            top_num = max(arr[i][j], top_num)

    top_list = []
    for i in range(map_size):
        for j in range(map_size):
            if arr[i][j] == top_num:
                top_list.append((i,j))
    
    return top_list


def dfs(current_y, current_x, len, chance, board):
    global visited
    global max_length

    board = deepcopy(board)

    for y, x in dyx:
        ny, nx = current_y + y, current_x + x

        # 해당 좌표가 배열 범위를 벗어났다면 다음 방향의 좌표 생성
        if ny < 0 or nx <0 or  ny >= map_size or nx >= map_size: continue

        # 방문하지 않은 곳이라면
        if not visited[ny][nx]:
            # 현재 위치의 높이보다 다음 위치의 높이가 높은 경우
            if board[current_y][current_x] <= board[ny][nx]: 
                # 산을 깎았을 때 높이가 현재 높이보다 높은 경우
                # 찬스가 있어도 산을 깎는 것이 의미가 없음
                if board[ny][nx] - cut_num >= board[current_y][current_x]: continue

                # 깎으면 갈 수 있지만 찬스가 없음
                if not chance: continue

                # 여기에 도달한 값은 깎았을 때 이동이 가능한 좌표들
                # 찬스를 사용해서 높이를 깎고 이동
                temp = board[ny][nx]
                chance = False
                board[ny][nx] = board[current_y][current_x]-1   # 현재 값보다 하나 작은 값이 더 길게 이동할 수 있음
                visited[ny][nx] = 1  # 방문 체크
                dfs(ny, nx, len+1, chance, board)
                # 바뀐 값들 다시 원상복구
                chance = True
                visited[ny][nx] = 0
                board[ny][nx] = temp
                    
                
            # 현재 높이보다 낮은 경우 -> 그냥 이동 가능
            if board[current_y][current_x] > board[ny][nx]:
                visited[ny][nx] = 1
                dfs(ny, nx, len+1, chance, board)
                visited[ny][nx] = 0
        
    # pprint(visited)
    # print('len : ',len)
    max_length = max(max_length, len)
    # print('max : ',max_length)
    return


for tc in range(1, T+1):
    map_size, cut_num = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(map_size)]
    visited = [[0] * map_size for _ in range(map_size)]
    # print(board)
    max_length = 0

    # 가장 높은 지점의 좌표들 찾아서 리스트로 반환
    top_list = top_point(board)

    # 가장 높은 지점들만 dfs돌기
    for start_y, start_x in top_list:
        # 시작 지점 방문처리
        # print('------------------------------------------------------------')
        visited[start_y][start_x] = 1
        dfs(current_y =  start_y, current_x = start_x, len=1, chance=True, board=board)
        # 방문처리 원복
        # 원복 해줘야 다음 좌표에 대해 DFS를 돌 때 해당 좌표가 방문상태가 아니게 됨
        visited[start_y][start_x] = 0

    print(f'#{tc} {max_length}')
