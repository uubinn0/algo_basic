'''
대표자가 아닌 노드를 기준으로 다른 그룹과 합칠 때
해당 노드 이외의 다른 노드 + 대표자의 대표자가 변경되지 않는 문제가 있었음.

ex. 12 34 41인 경우
마지막에 4와 1을 붙일 때 3의 헤드가 1로 바뀌지 않고 그대로 3으로 유지 됨.

해결하기 위해서 대표자의 대표자 리스트 값을 바꿔주고 난 이후
자기자신이 대표자가 아닌 값은 해당 대표자의 대표자값으로 한 번 더 변경해줌
'''


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

        if a_head == b_head :continue
        # 작은 수를 대표자로 설정할 것임
        # 따라서 큰 수의 대표자 리스트 값을 작은 수로 변경
        if a_head < b_head:
            head_list[b_head] = a_head
        else:
            head_list[a_head] =  b_head
        # print(head_list)
        for j in range(N + 1):
            if j != head_list[j]:
                head_list[j] = find_head(head_list[j])

        # print('->',  head_list)


    # print(head_list)
    group_cnt = len(set(head_list)) -1

    print(f'#{tc} {group_cnt}')
        


