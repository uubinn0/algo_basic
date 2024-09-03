'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZGtlGm6ROIDFAQP&contestProbId=AV15Khn6AN0CFAYD&probBoxId=AZGtlRgqRPADFAQP&type=PROBLEM&problemBoxTitle=20240903&problemBoxCnt=1
'''

T = int(input())


def dfs(num_list, c_cnt):
    global max_num
    global visited

    # 교환 횟수를 모두 소진한 경우에만 최대값을 확인해야함
    if c_cnt == 0:
        make_num = ''.join(num_list)
        max_num = max(max_num, int(make_num))  # 최대 값 갱신
        return


    # 한 자리 고정하고 다른 자리를 계속 바꿔가며 숫자 찾기
    for i in range(len(num_list)-1):
        for j in range(i+1, len(num_list)):

            # 숫자 위치 교환하기
            num_list[i], num_list[j] = num_list[j], num_list[i]
            make_num = ''.join(num_list)

            # 이미 만든 적 있는 숫자인 경우
            if (make_num, c_cnt) in visited: return

            # 방문한 적 없는 경우
            visited.add((make_num,c_cnt))
            dfs(num_list, c_cnt-1)

            # 복원
            num_list[i], num_list[j] = num_list[j], num_list[i]


for tc in range(1, T+1):
    num_list, change_cnt = map(str, input().split())
    num_list = [str(num_list[i]) for i in range(len(num_list))]
    # print(num_list, type(num_list[0]))
    visited = set()
    max_num = 0

    dfs(num_list, int(change_cnt))

    print(f'#{tc} {max_num}')
