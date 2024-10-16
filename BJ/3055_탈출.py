R, C = map(int, input().split())

board = [list(input()) for _ in range(R)]
print(board)

for i in range(R):
    for j in range(C):
        if board[i][j] == 'S':
            start_point = (i, j)
            break

print(start_point)