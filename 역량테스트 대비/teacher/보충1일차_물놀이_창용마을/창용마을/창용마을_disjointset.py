import sys
sys.stdin = open('s_input.txt')
"""
# 최적화 전 find_set
def find_set(x):
    if x == p[x]:  # 노드 x가 자기 자신을 부모 노드로 가지는 경우 그대로 반환 
        return x
    return find_set(p[x])  # 부모 노드를 재귀적으로 찾고 반환
"""

# 경로 압축을 적용한 find_set
def find_set(x):
    if x != p[x]:  # 노드 x가 자기 자신을 부모로 가지지 않는 경우
        p[x] = find_set(p[x])  # 부모 노드를 재귀적으로 찾고 경로 압축 수행
    return p[x]

"""
# 최적화 전 union 함수
def union(x, y):
    px = find_set(x)  # 노드 x의 대표자(부모) 찾기
    py = find_set(y)  # 노드 y의 대표자(부모) 찾기

    if px < py:  # 값이 더 작은 부모가 큰 부모에게 union
        p[py] = px
    else:
        p[px] = py
"""

# 랭크를 이용한 union 함수
def union(x, y):
    px = find_set(x)  # 노드 x의 대표자(부모) 찾기
    py = find_set(y)  # 노드 y의 대표자(부모) 찾기

    if px != py:  # 두 노드가 서로 다른 집합에 속해 있는 경우에만 합침
        if rank[px] > rank[py]:  # 랭크가 높은 트리에 붙임
            p[py] = px
        elif rank[px] < rank[py]:
            p[px] = py
        else:
            p[py] = px  # 랭크가 같은 경우 하나를 다른 하나의 부모로 설정
            rank[px] += 1  # 랭크 증가



T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    p = [i for i in range(N+1)]
    rank = [0] * (N+1)

    for _ in range(M):
        a, b = map(int, input().split())
        union(a, b)

    for i in range(1, N + 1):
        find_set(i)

    print(f"#{test_case} {len(set(p)) - 1}")
