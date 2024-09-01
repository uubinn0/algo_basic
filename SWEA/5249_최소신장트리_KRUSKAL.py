'''
최소 가중치 간선을 선택하는 알고리즘

KRUSKAL 알고리즘
1. 가중치 기준 오름차순 정렬
2. 가장 가중치가 작은 두 간선에 연결된 두 정점의 대표자 비교
    2-1. 대표자가 다른 경우 두 간선을 합친다. -> 가중치 더해주고 대표자도 바꿔줌
    2-2. 대표자가 같은 경우 이미 연결된 정점들 -> 연결하지 않고 넘어간다.
'''

T = int(input())


def find_head(arr, x):
    if x != arr[x]:
        arr[x] = find_head(arr, arr[x])
    return arr[x]


def kruskal(arr):
    cost = 0
    head = [i for i in range(V+1)]

    for start_v, end_v, weight in arr:
        a_head = find_head(head, start_v)
        b_head = find_head(head, end_v)

        # 두 정점의 대표자가 다른 경우
        if a_head != b_head:
            # 더 작은 쪽을 대표자로
            # 이 때 대표자의 대표자 값끼리 비교해야 함
            if head[a_head] > head[b_head]:
                head[a_head] = b_head
            elif head[a_head] < head[b_head]:
                head[b_head] = a_head

            # print('->', head)

            cost += weight
            # print(f'w: {weight}, c: {cost}')
    
    return cost


for tc in range(1,T+1):
    V, E = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    arr.sort(key=lambda x: x[2])
    # print(arr)

    result = kruskal(arr)

    print(f'#{tc} {result}')