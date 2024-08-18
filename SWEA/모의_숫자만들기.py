import sys
sys.stdin = open('./input/숫자만들기_input.txt', 'r')

T = int(input())


def make_num(idx, op_list, current_sum):
    global max_total
    global min_total

    # 모든 연산자를 다 사용한 경우
    if idx == N-1:
        min_total = min(min_total, current_sum)
        max_total = max(max_total, current_sum)
        return
    
    for i in range(len(op_list)):
        # 연산자를 사용 횟수가 남아 있다면
        if op_list[i] != 0:
            op_list[i] -= 1 # 횟수 차감해주고
            if i == 0:
                make_num(idx+1, op_list, current_sum+num_list[idx+1])
            elif i == 1:
                make_num(idx+1, op_list, current_sum-num_list[idx+1])
            elif i == 2:
                make_num(idx+1, op_list, current_sum*num_list[idx+1])
            elif i == 3:
                make_num(idx+1, op_list, int(current_sum/num_list[idx+1]))
            op_list[i] += 1 # 횟수 원래대로 돌려줌


for tc in range(1, 1+T):
    N = int(input())
    op_list = list(map(int,input().split()))
    num_list = list(map(int,input().split()))
    max_total = -float('inf')
    min_total = float('inf')

    make_num(idx=0, op_list=op_list, current_sum=num_list[0])

    
    # print(f'{max_total, min_total}')
    print(f'#{tc} {max_total - min_total}')