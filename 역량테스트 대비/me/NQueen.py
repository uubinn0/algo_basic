'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GKs06AU0DFAXB

퀸의 경우 가로 세로 대각선으로 공격을 한다.
퀸을 y,x에 놓을 경우 y의 모든 열에는 놓을 수 없게 됨
또한 x열에는 놓을 수 없게 됨

따라서 dfs에서 행을 증가시키며 넘겨주자.
dfs에서는 해당 열에 둘 수 있는지 검사?
'''


T = int(input())

dyx = [[-1,-1], [-1,1], [1,1], [1,-1]]


def dfs(visited_y, visited_x, visited, idx):
    global cnt

    # 모든 퀸을 다 놓았을 때
    if idx == N:
        cnt +=1
        return

    # 각 좌표를 순환하며 퀸을 놓는다.
    for cy in range(N):
        # 해당 행이 이미 다른 퀸의 영역이라면
        if cy in visited_y: continue

        for cx in range(N):
            # 해당 열이 이미 다른 퀸의 영역이라면
            if cx in visited_x: continue

            # 놓을 수 있는 영역이라면 해당 좌표를 방문처리
            visited_y.add(cy)
            visited_x.add(cx)

            # 대각선 처리하기
            # 현재 좌표를 기준으로 왼쪽 위, 오른쪽 위, 오른쪽 아래, 왼쪽 아래 대각선에 대한 좌표를 만든다.
            for dy, dx in dyx:
                ny, nx = cy + dy, cx + dx

                # 새 좌표가 범위를 벗어나지 않을 경우까지
                while 0 <= ny < N and 0<= nx < N:
                    if (ny, nx) in visited:
                        break
                    visited.add((ny, nx))   # 해당 좌표를 방문처리
                    ny, nx = ny + dy, nx + dx

            dfs(visited_y, visited_x, visited, idx+1)

            # 복원
            visited_y.remove(cy)
            visited_x.remove(cx)

            for dy, dx in dyx:
                ny, nx = cy + dy, cx + dx

                # 새 좌표가 범위를 벗어나지 않을 경우까지
                while 0 <= ny < N and 0<= nx < N:
                    visited.remove((ny, nx))   # 해당 좌표를 방문처리
                    ny, nx = ny + dy, nx + dx



for tc in range(1, T+1):
    N = int(input())
    visited_y = set()
    visited_x = set()
    visited = set()
    # print(visited)
    cnt = 0

    dfs(visited_y, visited_x, visited, idx = 0)

    print(cnt)