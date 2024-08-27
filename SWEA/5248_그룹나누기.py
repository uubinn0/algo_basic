T = int(input())


def find_head(x):
    if x != head_list[x]:
        head_list[x] = find_head(head_list[x])
    return head_list[x]


for tc in range(1, T+1):
    # N : 출석번호 끝 => 노드 수
    # M : 신청서 수 => 간선 수
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    head_list = [x for x in range(N+1)]

    # 간선의 수 만큼 돌면서 각 노드들을 확인
    for i in range(M):
        a, b = arr[i*2], arr[i*2+1]
        a_head = find_head(a)
        b_head = find_head(b)

        # 작은 수를 대표자로 설정할 것임
        # 따라서 큰 수의 대표자 리스트 값을 작은 수로 변경
        if a_head < b_head:
            head_list[b] = a_head
        else:
            head_list[a] =  b_head
    
    # 부모의 대표자와 자식의 대표자가 같은지 확인 후
    # 다른 경우 자식의 대표자를 변경해줌
    for i in range(N+1):
        if i != head_list[i]:
            head_list[i] = find_head(head_list[i])

    # print(head_list)
    group_cnt = len(set(head_list)) -1

    print(f'#{tc} {group_cnt}')
        


