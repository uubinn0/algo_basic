'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXWXMZta-PsDFAST
'''

from collections import deque

T = int(input())


dyx = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def bfs(deq):



for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    # W 좌표를 담을 데크
    deq = deque()
    
    # W 찾기
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'W':
                deq.append((i, j))


    # W 좌표들에 대해서 bfs로 탐색하며 L까지의 최소값 찾음
    result = bfs(deq)

    print(f'#{tc} {result}')