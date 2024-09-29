'''
https://www.acmicpc.net/problem/13023
신장트리인지 확인하는 문제
사이클이 있다면 신장트리가 아님
사이클이 있다? => 간선의 수가 노드의 수 -1보다 크다는 의미
-----
A->B->C->D->E의 관계가 있는지 확인
5명이 이런 관계를 갖기만 하면 됨
'''
from collections import defaultdict

N, M = map(int, input().split())

if N < 4:
    print(0)
    quit()

relations = defaultdict(list)
result = 0

for i in range(M):
    a, b = map(int, input().split())
    relations[a].append(b)
    relations[b].append(a)

# print(relations.items())


def search(current_node, visited, depth):
    # 현재 노드가 방문한 적 있다면 함수 종료
    if current_node in visited: return depth

    # 관계가 4번이상 이어지면
    if depth >= 4:  return depth

    # 방문 처리
    visited.add(current_node)

    # 현재 노드의 인접 노드로
    for adj_node in relations[current_node]:
        res = search(adj_node, visited, depth+1)
        if res >= 4:
            return res

    visited.remove(current_node)

    return depth


# 모든 노드에 대해서 해당 관계가 있는지 확인
for search_node in relations.keys():
    result = search(search_node, set(), 0)

    if result >= 4:
        print(1)
        quit()

if result < 4:
    print(0)