'''
https://www.acmicpc.net/problem/11651

엥 문제 말을 이해를 못 하겠음
아 지금 이해함
설명 정말 못 하네ㅋㅋ

y좌표를 기준으로 정렬을 한다.
이 때 동일한 y좌표를 갖는 점이 있는 경우
x좌표를 기준으로 정렬한다.
'''

N = int(input())

points = [tuple(map(int, input().split())) for _ in range(N)]
# print(point)
x_list = [point[0] for point in points]
y_list = [point[1] for point in points]

while x_list:
    # 최소 y좌표
    min_y = min(y_list)

    