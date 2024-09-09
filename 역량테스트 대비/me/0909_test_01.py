'''
주어진 과목을 모두 수강할 경우 몇 학기가 소요되는지 구하시오.
주어진 과목을 모두 수강할 수 없는 경우 -1을 반환



'''
import sys
sys.stdin = open('0909_01_input.txt', 'r')

from collections import defaultdict

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    adj_dict = {i: [] for i in range(1, N + 1)}
    pre_subject = {i: [] for i in range(1, N + 1)}

    # 인접한 정점 그래프
    for i in range(0, N):
        for j in arr[i][1:]:
            adj_dict[j].append(i+1)
    print(adj_dict)

    # 해당 과목 : 선수과목 리스트
    for i in range(0, N):
        for j in arr[i][1:]:
            pre_subject[i+1].append(j)
    print(pre_subject)


