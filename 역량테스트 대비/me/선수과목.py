'''
1
4
1 3
2 1 3
1 4
0
'''

from collections import defaultdict, deque

T = int(input())

for tc in range(1, T+1):
    N = int(input())    # 과목 수
    need_cnt = defaultdict(int)
    next_pre = defaultdict(list)
    pre_next = defaultdict(list)
    no_need_pre = list()

    for i in range(1, N+1):
        temp_list = list(map(int, input().split()))

        for j in range(len(temp_list)):
            if j == 0:
                need_cnt[i] = temp_list[j]
                if temp_list[j] == 0:
                    no_need_pre.append((i,1))
            if j != 0:
                next_pre[i].append(temp_list[j])
                pre_next[temp_list[j]].append(i)

    # print(need_cnt)
    # print(next_pre)
    # print(pre_next)
    # print(no_need_pre)

    # 선행 이수 과목이 필요 없는 과목 => need_cnt == 0
    deq = deque(no_need_pre)
    # max_cnt = 0

    while deq:
        finished_subject, cnt = deq.popleft()
        # print(finished_subject, cnt)

        # 해당 과목의 선이수 과목이 있는 경우 pass
        if need_cnt[finished_subject] != 0: continue

        # 해당 과목을 들엇을 때 이수할 수 있는 과목의 이수 과목 수를 체크
        for next in pre_next[finished_subject]:
            need_cnt[next] -= 1 # 선이수 조건 하나 제거
            if need_cnt[next] == 0: # 선이수 조건을 모두 달성했다면
                deq.append((next, cnt+1))

        # max_cnt = max(max_cnt, cnt)

    for key, value in need_cnt.items():
        if value != 0:
            cnt = -1

    print(f'#{tc} {cnt}')