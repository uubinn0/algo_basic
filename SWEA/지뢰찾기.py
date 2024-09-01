from copy import deepcopy
from collections import deque
from pprint import pprint

T = int(input())

dyx = [[-1,0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1,], [-1, 0], [-1, -1]]


def bfs(arr, current_position):
    global min_click
    click_cnt = 0
    arr = deepcopy(arr)
    pprint(arr)

    deq = deque([current_position])

    while deq:
        cy,cx = deq.popleft()

        # 방문하거나 연쇄적으로 숫자 표시가 된 적 없는 좌표인 경우
        if arr[cy][cx] == '.':
            arr[cy][cx] = 0 # 방문 표시
            click_cnt += 1  # 클릭 카운트 증가

            # 8방향 탐색
            for y, x in dyx:
                ny, nx = cy+y, cx+x

                # 인접 좌표가 범위를 벗어난 경우 다음 좌표 탐색
                if ny < 0 or nx < 0 or ny >= N or nx >= N: continue

                # 인접 좌표가 폭탄인 경우 현재 좌표에 인근 폭탄 카운트 증가
                if arr[ny][nx] == '*':
                    arr[cy][cx] +=1

                # 인접 좌표가 폭탄이 아닌 경우 
                # 탐색할 좌표 후보임
                # 다음 탐색을 위해 해당 좌표를 큐에 넣음
                if arr[ny][nx] == '.':
                    deq.append((ny,nx))

            pprint(arr)

    # 다 클릭하고 난 후 안 눌린 . 하나하나 눌러 줌
    for line in arr:
        click_cnt += line.count('.')

    min_click = min(min_click, click_cnt)
    return
                


for tc in range(1, T+1):
    N = int(input())
    arr = []
    min_click = float('inf')

    for _ in range(N):
        text = input()
        temp = []
        for str in text:
            temp.append(str)
        arr.append(temp)

    for y in range(N):
        for x in range(N):
            # 지뢰가 아닌 좌표에 대해서 bfs 돌기
            if arr[y][x] != '*':
                print(y,x)
                bfs(arr, (y,x))
                print(min_click)

    print(f'#{tc} {min_click}')