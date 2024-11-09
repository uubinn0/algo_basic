'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15PTkqAPYCFAYD
'''

# import sys
# sys.stdin = open()
from collections import defaultdict
from collections import deque

T = int(input())
for i in range(1, 1+T):
    V, E, num1, num2 = map(int, input().split())
    child_parent = defaultdict(list)
    parent_child = defaultdict(list)

    # 입력 받아 {자식 : 부모} , {부모 : 자식} 형태의 딕셔너리로 만들기
    temp_list = list(map(int, input().split()))
    for j in range(0, E*2, 2):
        child_parent[temp_list[j+1]].append(temp_list[j])
        parent_child[temp_list[j]].append(temp_list[j+1])

    # print(child_parent)
    # print(parent_child)


    # 공통 조상 찾기
    # 1. 한 쪽의 부모 찾기
    def find_parents(n, graph, parent=[]):
        if graph[n]:
            parent.append(graph[n][0])

            if graph[n][0] in graph.keys():
                return find_parents(graph[n][0], graph, parent)

            return parent

    num1_parents = set(find_parents(num1, child_parent))
    # print(num1_parents)


    # 2. 다른 한 쪽도 부모를 찾으며 올라감
    # 이 때 반대편 부모 set과 비교하며 공통된 부모가 존재하는지 확인함
    # 존재하는 경우 해당 부모가 가장 깊은 곳에 있는 공통 부모이므로 반환
    def find_common_parent(n, graph):
        if graph[n]:
            if graph[n][0] in num1_parents:
                return graph[n][0]

            return find_common_parent(graph[n][0], graph)

    common_parent = find_common_parent(num2, child_parent)


    # 3. 서브 트리 사이즈 구하기
    # bfs 형식으로 탐색하며 total_size에 크기 더해줌
    total_size = 1
    deq = deque([common_parent])

    while deq:
        head_node = deq.popleft()
        total_size += len(parent_child[head_node])

        for item in parent_child[head_node]:
            # 자식이 있는 경우만 큐에 넣어줌
            if item in parent_child.keys():
                deq.append(item)

    print(f'#{i} {common_parent} {total_size}')
