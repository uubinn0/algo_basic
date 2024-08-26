'''
1. N번의 구슬을 쏠 수 있다.
2. 가로 W, 세로 H의 보드에 벽돌이 있으며 해당 벽돌에는 영향력이 적혀있다.
3. 구슬이 벽돌을 쳤을 때 상하좌우로 각 벽돌의 영향력 -1 칸만큼 제거된다.
4. 제거될 때 다른 벽돌을 파괴했을 때 해당 벽돌의 영향력만큼 다시 다른 벽돌을 제거할 수 있다.
5. 제거되고 난 후에는 벽돌들은 아래로 떨어져 정렬된다.

남은 벽돌의 개수를 구하라!
====
모든 벽돌에 구슬을 쏴서 최대 값을 구하면 될 거 같음.
구슬을 쏘기 위해서는 벽돌의 위치를 알아야 함.


'''

import sys
from pprint import pprint
sys.stdin = open('./input/벽돌_input.txt', 'r')

T = int(input())

dyx = [[-1,0], [0, 1], [1,0], [0,-1]]


def shoot(shoot_cnt, board, destroy_brick_cnt):
    global total_destroy_cnt

    # 모든 구슬 사용 횟수를 소진한 경우
    if  shoot_cnt == N:
        total_destroy_cnt = max(total_destroy_cnt, destroy_brick_cnt)
        return
    
    '''
    구한 벽돌 좌표로 접근해서 해당 벽돌의 영향력을 확인
    상하좌우 영향력-1 범위만큼 탐색하며 연쇄적으로 파괴되는 벽돌을 찾는다.
    인접한 벽돌들을 계속해서 탐색하기 때문에 bfs로 접근 
    '''


    

    


for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]
    total_destroy_cnt = 0
    # pprint(board)


    copy_board = [arr[:] for arr in board]
    # pprint(copy_board)

    # 가장 상단의 벽돌의 좌표 구하기
    # 구한 좌표는 큐에 넣으면 될 거 같음
    for arr in board:
        for brick in arr:
            if brick:
                pass
    
    # 구슬을 쏜다.
    shoot(shoot_cnt = 0, board = copy_board, destroy_brick_cnt = 0)