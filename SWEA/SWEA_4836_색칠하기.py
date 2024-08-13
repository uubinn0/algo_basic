from pprint import pprint

T = int(input())

for test_case in range(1, T+1):
    box_cnt = int(input())
    box_list = [list(map(int, input().split())) for _ in range(box_cnt)]
    # print(box_list)
    board = [[0] * 10 for _ in range(10)]
    result = 0
    # pprint(board)
    

    for box in box_list:    # 각 박스별로 좌표를 채울 예정
        # 박스의 좌표 받아오기
        top_y, top_x = box[0], box[1]
        bottom_y, bottom_x = box[2], box[3]
        color = box[4]

        for height in range(top_y, bottom_y+1):   # 사각형 채우기 - 세로
            for width in range(top_x, bottom_x+1):
                board[height][width] += color
    #     print(box)
    #     pprint(board)

    # pprint(board)

    for line in board:
        result += line.count(3)
    
    print(f'#{test_case} {result}')
        
    


