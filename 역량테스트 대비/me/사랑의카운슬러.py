'''
방향값도 같이 넣어야 하는 문제 같은데?
'''
T = int(input())

def dfs(arr, total_move):
    global min_total_move
    # 탈출 조건
    
    if len(arr) == 2:
        ax, ay = arr[0]
        bx, by = arr[1]

        total_move = 

        min_total_move = min(min_total_move, total_move)
        return
    
    for i in range(0, len(arr)-1, 2):
        for j in range(i+1, len(arr)):
            ax, ay = arr[i]
            bx, by = arr[j]

            # 해당 좌표들의 벡터 크기
            total_move += 
            dfs(arr[j+1:], total_move)
            total_move -=

    




for tc in range(1, T+1):
    N = int(input())
    arr = set(tuple(map(int,input().split())) for _ in range(N))
    min_total_move = float('inf')

    dfs(arr, total_move = 0)
