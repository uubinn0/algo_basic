'''
주어진 과목을 모두 수강할 경우 몇 학기가 소요되는지 구하시오.
주어진 과목을 모두 수강할 수 없는 경우 -1을 반환



'''
import sys
from collections import deque
from collections import defaultdict

# sys.stdin = open('0909_01_input.txt', 'r')


# 해당 과목의 선수 과목을 모두 이수한 상태인지 확인하는 함수
def check(sub_num):
    for pre_sub in pre_subject[sub_num]:
        # 선수과목을 이미 들은 상태인 경우
        if pre_sub in visited:
            continue
        else:
            return False
    return True

def search(start_list):
    global cnt

    # 선수과목이 없는 과목이 없는 경우
    if not start_list:
        cnt = -1
        return

    # 선수과목이 없는 과목들은 이수한 것으로 치고 학기 +1 해줌
    for none_pre_sub in start_list:
        visited.add(none_pre_sub)
    cnt+=1

    # 시작 지점이 된 과목을 들었을 때 이수할 수 있는 과목을 찾기
    # 인접 리스트에서 현재 학기에서 이수한 과목이 키값인 value를 저장
    next_sub_list = []
    for start_sub in start_list:
        for next_sub in adj_dict[start_sub]:
            next_sub_list.append((next_sub, cnt+1))
    next_sub_deq = deque(next_sub_list)


    while next_sub_deq:
        next_sub, semester = next_sub_deq.popleft()

        # 이수할 수 없는 상황인 경우 = 아직 선수과목이 남아있는 상태
        if not check(next_sub):
            next_sub_deq.append((next_sub, semester+1))  # 다음 학기에 듣는 것으로 처리

        # 선수과목을 모두 방문한 경우 해당 과목을 이수한 것(방문)으로 처리
        # 해당 과목을 이수한 이후 들을 수 있는 과목들을 다음 학기에 듣는 것으로 처리해서 큐에 넣어줌
        visited.add(next_sub)
        cnt = semester

        for adj_sub in adj_dict[next_sub]:
            next_sub_deq.append((adj_sub, semester + 1))

    return



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    adj_dict = {i: [] for i in range(1, N + 1)}
    pre_subject = {i: [] for i in range(1, N + 1)}
    visited = set()
    cnt = 0 # 학기

    # 인접한 정점 그래프
    for i in range(0, N):
        for j in arr[i][1:]:
            adj_dict[j].append(i+1)
    print(adj_dict)

    # 해당 과목 : 선수과목 리스트
    for i in range(0, N):
        for j in arr[i][1:]:
            pre_subject[i+1].append(j)
    print(pre_subject)

    start_list = []
    for key, value in pre_subject.items():
        # 만약 값이 비어있다면 선수과목이 없는 과목
        # 시작 지점이된다.
        if not value:
            start_list.append(key)
    # print(start_v)

    search(start_list)
    print(cnt)