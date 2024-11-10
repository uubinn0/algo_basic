'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeUtVakTMDFAVH
'''
from itertools import combinations


def make_food(ings):
    total_power = 0
    for i, j in combinations(ings, 2):
        # print('재료', board[i][j], board[j][i])
        total_power += board[i][j] + board[j][i]
    return total_power


T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    min_chai = float('inf')
    total_item = set(range(N))  # 전체 재료 모음 set

    # a 음식에 들어갈 재료 고르기
    for a_picks in combinations(total_item, N//2):
        # 전체 재료 set에서 a에 들어간 재료들 제거 = b 재료
        b_picks = total_item - set(a_picks)
        # print(a_picks, b_picks)

        a_power = make_food(a_picks)
        b_power = make_food(b_picks)

        min_chai = min(min_chai, abs(a_power - b_power))

    print(f'#{tc} {min_chai}')