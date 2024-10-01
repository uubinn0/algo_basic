'''
https://www.acmicpc.net/problem/18111


땅을 고르게 하는 방법 2가지
1. 블록을 제거한다 => 2초
2. 블록을 추가한다 => 1초

소지한 블록의 수가 B로 주어진다

1. 각 칸에 대해서 어떤 방법을 쓸 것인지. 선택
2. 해당 방법을 통해 가장 낮은 높이가 모두 동일한지 높이 체크
3. 동일한 높이라면 해당 방법을 통해 구한 방법이 최소 소요 시간인지 확인

'''

N, M, B = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
total_min_time = float('inf')

# 가장 높은 높이와 낮은 높이 찾기
def find_height(brd):
    low_h = float('inf')
    high_h = -1

    for arr in brd:
        high_h = max(max(arr), high_h)  # 각 행에서 가장 큰 수를 찾아서 이전 수와 비교
        low_h = min(min(arr), low_h)

    return low_h, high_h


low, high = find_height(board)
# print(low, high)


# 높이에 따라서 경우가 나뉨
# 가장 낮은 높이라면 블록을 추가할 것인지 말 것인지 선택
# => 블록을 추가할 것이라면 몇 개를 추가할 것인지 => 인벤에 있는 블록 수도 고려해야 함
# 가장 낮은 높이가 아니라면 그대로 두거나 높이를 깎거나 중 선택
# 음.. 기준 높이를 정하고 해당 높이를 만들 때 소요되는 시간과 블록 수를 계산하는 방법?
# 기준 높이는 가장 낮은 높이 ~ 가장 높은 높이
# 음........ 근데 시간이 1초고 높이는 최대 256까지인데 시간 초과날 거 같음


def ground(target_h):
    pass



for target_h in range(low, high+1):
    ground(target_h)