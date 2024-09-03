T = int(input())


def find_head(x, head):
    if x != head[x]:
        head[x] = find_head(head[x], head)
    return head[x]


for tc in range(1, T+1):
    N, M = map(int,input().split()) # 정점 수, 간선 수

    arr = [list(map(int, input().split())) for _ in range(M)]

    graph = {i : [] for i in range(1, N+1)}

    # 인접리스트 만들기
    for start_v, end_v in arr:
        graph[start_v].append(end_v)
        graph[end_v].append(start_v)

    # print(graph)

    # 대표자 리스트
    head = [ i for i in range(N+1)]

    # 대표자 비교 후 숫자가 작은 것을 대표자로 변경하며 그룹 합치기
    for start_v in range(1, N+1):
        for end_v in graph[start_v]:
            # 두 정점의 대표자를 확인
            a_head = find_head(start_v, head)
            b_head = find_head(end_v, head)

            # 대표자가 다를 때
            # 대표자의 크기가 더 작은 것을 대표자로 채택
            if a_head < b_head:
                head[b_head] = a_head
            elif a_head > b_head:
                head[a_head] = b_head
            
            # print(head)

            # for i in range(1, N+1):
            #     if i != head[i]:
            #         head[i] = find_head(head[i], head)

            # print('->',head)

    # 대표자와 자기 자신이 같은 경우가 그룹의 대표
    # 그룹의 대표 수를 세면 그룹의 수와 같다
    result = 0
    for i in range(1, N+1):
        if head[i] == i:
            result += 1

    # result = len(set(head)) -1
    print(f'#{tc} {result}')
