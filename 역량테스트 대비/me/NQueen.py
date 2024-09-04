'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GKs06AU0DFAXB
'''


T = int(input())


def dfs(idx, visited):
    global cnt

    # 모든 좌표가 놓을 수 없는 자리면
    if all(visited): return

    # 모든 퀸을 다 놓은 경우 끝
    if idx > N: 
        cnt += 1
        return

    for i in range(N):
        for j in range(N):
            # 놓을 수 없는 자리이면
            if visited[i][j] == True: continue

            # 해당 좌표에 놓을 수 있다면
            # 가로, 세로, 대각선 방문처리
            for k in range(N):
                visited[i][k] = True    # 가로 방문처리
                visited[k][j] = True    # 세로 방문처리

            
            # 대각선 방문처리

            dfs(idx+1, visited)

            # 복원
            


for tc in range(1, T+1):
    N = int(input())
    visited = [[False] * N for _ in range(N)]
    # print(visited)
    cnt = 0

    dfs(idx = 0, visited=visited)