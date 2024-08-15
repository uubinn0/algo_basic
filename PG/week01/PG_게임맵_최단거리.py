'''
https://school.programmers.co.kr/learn/courses/30/lessons/1844
'''

import sys
import copy
from collections import deque
from pprint import pprint

sys.stdin = open('./input/게임맵_input.txt')

T = int(input())

# 4방향 이동
dyx = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def search(y, x, cnt,visited):

    # # 도착 지점 주변이 막힌 경우 - 가지치기하고 싶은데 이거 넣으면 사이트에서 오류남 엌ㅋㅋ
    # # 생각하기 귀찮으니까 일단 뺌
    # if visited[N-1][M-2] == 0 and visited[N-2][M-1] == 0:
    #     return -1

    deq = deque()
    deq.append((y,x, 1))
    visited[y][x] = 2   # 방문처리

    while deq:
        y, x, cnt= deq.popleft()

        # 도착 지점이면?
        if y == M-1 and x == N-1:
            return cnt

        for i, j in dyx:
            # 새 좌표
            new_y = y + i
            new_x = x + j

            # out of range
            if new_x < 0 or new_y < 0 or new_x >= N or new_y >= M:
                continue
            
            # 벽인 경우
            if visited[new_y][new_x] == 0:
                continue

            # 방문한 곳인 경우
            if visited[new_y][new_x] == 2:
                continue

            # 갈 수 있는 좌표라면
            deq.append((new_y, new_x, cnt+1))  # 큐에 넣고
            visited[new_y][new_x] = 2   # 방문 처리

    # pprint(visited)
    # print(cnt)



for test_case in range(1, 1+T):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    # print(board)
    visited = copy.deepcopy(board)

    result = search(y=0, x=0, cnt=0, visited=visited)
    print(result)