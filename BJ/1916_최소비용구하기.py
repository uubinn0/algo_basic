'''
https://www.acmicpc.net/problem/1916

최소비용
음수 없음
다익스트라
시작 지점에 한 노드에 대해서 각 노드까지의 최소 비용을 구함
기존 구했던 최소 비용에 다음 비용을 더하고 비교하여 최소인 경우 갱신하는 방식
'''
from collections import defaultdict
import heapq

CITY_NUM = int(input())
BUS_NUM = int(input())
bus_graph = defaultdict(list)

for _ in range(BUS_NUM):
    temp = list(map(int, input().split()))
    bus_graph[temp[0]].append((temp[1], temp[2]))

target_s, target_e = map(int, input().split())
# print(bus_graph)
# print(target_s, target_e)

INF = float('inf')
min_cost = [INF] * (CITY_NUM+1)
min_cost[target_s] = 0  # 시작 지점 0 초기화

min_heap = []
heapq.heappush(min_heap, (target_s, 0))

while min_heap:
    start, cost = heapq.heappop(min_heap)

    # 기존 비용이 현재 비용보다 작은 경우 넘어감
    # 같은 경우까지 포함하면 첫 번째 노드에서 넘어가지 않음
    if min_cost[start] < cost: continue

    # 인접 노드에 대해
    for adj_stop, adj_cost in bus_graph[start]:
        temp_cost = cost + adj_cost
        if temp_cost < min_cost[adj_stop]:  #
            min_cost[adj_stop] = temp_cost
            heapq.heappush(min_heap, (adj_stop, temp_cost))

# print(min_cost)
print(min_cost[target_e])