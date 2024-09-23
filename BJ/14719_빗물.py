'''
https://www.acmicpc.net/problem/14719

음 하나도 모르겠고

0번과 W-1 인덱스에는 물이 고일 수 없다

1. 배열을 만들어서 벽인 부분은 1로 채우자

'''

H, W = map(int, input().split())
brick = list(map(int, input().split()))

arr = [[0] * W for _ in range(H)]
# print(arr)

for i in range(W):
    