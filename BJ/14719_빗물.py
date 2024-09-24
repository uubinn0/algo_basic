'''
https://www.acmicpc.net/problem/14719

음 하나도 모르겠고

0번과 W-1 인덱스에는 물이 고일 수 없다

1. 배열을 만들어서 벽인 부분은 1로 채우자

'''

H, W = map(int, input().split())
brick = list(map(int, input().split()))
result = 0


# 좌우의 좌우의 가장 높은 벽 찾기
def find_wall(idx):
    left_max_height = 0
    right_max_height = 0

    # 왼쪽 벽 찾기
    for left_idx in range(idx-1, -1, -1):
        if left_max_height < brick[left_idx]:
            left_max_height = brick[left_idx]
            break

    for right_idx in range(idx+1, W):
        if right_max_height < brick[right_idx]:
            right_max_height = brick[right_idx]
            break

    return left_max_height, right_max_height


for i in range(1, W-1):
    left_wall, right_wall = find_wall(i)
    print(left_wall, right_wall)

    # 현재 인덱스에 세워진 벽의 높이가 양 옆 벽의 높이보다 높거나 같은 경우
    if left_wall <= brick[i] or right_wall <= brick[i]: continue

    result += min(left_wall, right_wall) - brick[i]

print(result)