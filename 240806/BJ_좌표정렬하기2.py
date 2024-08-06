'''
https://www.acmicpc.net/problem/11651

- 0805
y좌표를 기준으로 정렬을 한다.
이 때 동일한 y좌표를 갖는 점이 있는 경우
x좌표를 기준으로 정렬한다.

- 0806
튜플 형태로 감싸서 해당 좌표들을 리스트에 넣고 y좌표 기준으로 정렬.
동일한 값이 있는 경우 x 좌표 기준으로 정렬
'''

N = int(input())

# 튜플로 데이터 받기
points = [tuple(map(int, input().split())) for _ in range(N)]
# print(points)

# 리스트에 저장된 튜플 정렬하기
# points[1] 값 우선 정렬 후
# 동일한 값이 있는 경우 points[0]으로 정렬
points.sort(key=lambda x: (x[1], x[0]))

for point in points:
    print(*point)