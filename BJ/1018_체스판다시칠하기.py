'''
https://www.acmicpc.net/problem/1018

어케 보드 순환할건데
'''

N, M = map(int, input().split())
board = [list(map(str, input())) for _ in range(N)]
# print(board)
min_paint_cnt = float('inf')


for i in range(N):
    txt = ''
    for j in range(0, M-8):
        # print(j, j+8)
        txt += board[i][j]
    print(txt)