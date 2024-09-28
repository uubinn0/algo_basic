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

from Tools.scripts.findlinksto import visit

N, M = map(int, input().split())

relations = defaultdict(list)

for i in range(M):
    a, b = map(int, input().split())
    relations[a].append(b)
    relations[b].append(a)

# print(relations.items())

def search(current_node, visited, depth):
    # depth가 4가 되면?
    if depth == 4:
        return 1

    # 이미 방문한 노드라면
    if current_node in visited: return

    #  방문 체크
    visited.add(current_node)

    # 다음 방문할 노드 선정하기
    # 현재 노드의 인접한 노드로 이동
    for next_node in relations[current_node]:
        search(next_node, visited, depth+1)






for search_node in relations.keys():
    # print(search_node)
    search(search_node, set(), 0)
