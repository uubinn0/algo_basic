'''
22:45 ~ 23:14
완전 탐색으로 이차원 리스트를 돌며
각 범위에서 잡을 수 있는 파리의 수를 찾고
가장 많은 수를 구한다. 
'''

import sys
from pprint import pprint
sys.stdin = open('2001_input.txt', 'r')

T = int(input())


def update_max_kill(y, x):
    global max_kill

    # 파리 죽인 수 구하고
    # 기존 최대 죽인 수와 비교하여 갱신
    temp_kill = 0
    for i in range(M):
        # pprint(board[y+i][x:x+M])
        temp_kill += sum(board[y+i][x:x+M])

    max_kill = max(max_kill, temp_kill)
        

        


for test_case in range(1, T+1):
    # 리스트 크기 N / 파리채 크기 M
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    # print(board)
    max_kill = 0

    # 리스트를 돌며 max_kill 값을 최대 값으로 갱신하는 함수
    # 종료 조건 변수 : 초기 시작 지점 인덱스
    # 결과값 : 죽인 파리 수
    for y in range(N-M+1):
        for x in range(N-M+1):
            update_max_kill(y, x)

    print(max_kill)