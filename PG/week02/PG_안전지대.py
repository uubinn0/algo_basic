from pprint import pprint

def solution(board):
    N = len(board)  # 세로 길이
    M = len(board[0])   # 가로 길이
    cnt = 0
    
    # 8방향 탐색
    dyx = [[-1,0], [-1,1], [0, 1], [1,1], [1,0], [1, -1], [0, -1], [-1,-1]]
    
    pprint(board)
    
    for y in range(N):
        for x in range(M):
            
            # 폭탄인 경우만 8방향에 +2
            if board[y][x] == 1:
                for dy, dx in dyx:
                    new_y, new_x = y + dy, x + dx
                    
                    # 범위 똑바로 적자.... 
                    if 0 <= new_y < N and 0 <= new_x < M:

                        if board[new_y][new_x] != 1:
                            board[new_y][new_x] += 2
        
    pprint(board)

    for num_list in board:
        cnt += num_list.count(0)
    
    print(cnt)
    return cnt

solution([[0, 0, 0, 0, 1], [0, 1, 0, 1, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 1, 0, 0, 0]])