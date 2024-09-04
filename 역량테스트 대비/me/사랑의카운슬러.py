'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV2b_WPaAEIBBASw
'''
from collections import deque
from copy import deepcopy

T = int(input())

def dfs(arr, vector, visited):
    global min_total_move


    if all(visited):    # 모든 경우가 True인 경우
    # if len(arr) <= 2: # 리스트의 길이가 2인 경우 마지막이다.
    #     ax, ay = arr[0]
    #     bx, by = arr[1]
    #     vector.append((ax - bx, ay - by))
    #
    #     total_x, total_y = 0, 0

        # 모든 벡터값의 합 구하기
        for vxy in vector:
            vx, vy = vxy
            total_x, total_y = total_x + vx, total_y + vy

        vector_size = total_x**2 + total_y**2

        min_total_move = min(min_total_move, vector_size)
        return


    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            # print('arr: ', arr)

            # 방문한 경우
            if visited[i] and visited[j]: continue

            # 방문 체크
            visited[i] = True
            visited[j] = True

            # 좌표 2개 선택하고 짝을 지어준 애들의 벡터 값을 저장
            ax, ay = arr[i]
            bx, by = arr[j]

            # 벡터 계산
            vector.append((ax-bx, ay-by))
            # print('v : ', vector)

            # 좌표 2개를 제외한 리스트를 넘겨 다시 2개를 선택하게 함
            # temp = deepcopy(arr)  # 훼손 방지 복사
            # # print(temp)
            # temp.remove(arr[i])
            # temp.remove(arr[j])
            # print(temp)
            dfs(arr, vector, visited)

            # print('-> v : ', vector)
            # 복구
            vector.pop(-1)
            visited[i] = False
            visited[j] = False


for tc in range(1, T+1):
    N = int(input())
    arr = list(tuple(map(int,input().split())) for _ in range(N))
    min_total_move = float('inf')
    visited = [False] * len(arr)

    dfs(arr, [], visited)

    print(f'#{tc} {min_total_move}')
