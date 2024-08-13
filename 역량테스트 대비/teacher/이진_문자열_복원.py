import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T + 1):
    result = ''
    # 00, 01, 10, 11 <- 개수 나타내는 배열
    binary_cnt_list = list(map(int, input().split()))
    binary_types = ["00", "01", "10","11"]
    result = ''

    def dfs(cnt_list, string):
        global result

        # 이미 결과를 찾은 경우에는 return
        if result:
            return

        # 01 과 10 의 개수 차이가 2개 이상이라면 백트래킹
        if abs(cnt_list[1] - cnt_list[2]) > 1:
            return

        # 주어진 문자를 모두 사용한 경우, 문자가 제대로 완성됐고, 결과에 저장한다.
        if sum(cnt_list) == 0:
            result = string
            return

        # 마지막 문자가 0 으로 끝나는 경우에는 00, 01만 나올 수 있따.
        # 마지막 문자가 1 로 끝나는 경우에는 10, 11 만 나올 수 있따.
        if string[-1] == "0":
            if cnt_list[0] >= 1:
                # 00 으로 이어 붙이는 경우
                cnt_list[0] -= 1
                dfs(cnt_list, string + "0")
                cnt_list[0] += 1

            if cnt_list[1] >= 1:
                # 01 로 이어 붙이는 경우
                cnt_list[1] -= 1
                dfs(cnt_list, string + "1")
                cnt_list[1] += 1

        # 1 로 끝나는 경우에는 11, 10 온다.
        if string[-1] == "1":
            if cnt_list[3] >= 1:
                # 11 으로 이어 붙이는 경우
                cnt_list[3] -= 1
                dfs(cnt_list, string + "1")
                cnt_list[3] += 1

            if cnt_list[2] >= 1:
                # 10 로 이어 붙이는 경우
                cnt_list[2] -= 1
                dfs(cnt_list, string + "0")
                cnt_list[2] += 1

    # 주어진 00, 01, 10, 11 4개의 문자열로 시작하는 케이스에 대해서 모두 DFS 실행
    for idx in range(len(binary_types)):
        # idx에 해당하는 패턴의 개수가 1개 이상이여야 dfs를 실행할 수 있다.
        if binary_cnt_list[idx] >= 1:
            """
            파라미터 뭐로 하죠 ?
            1. 재귀호출을 끝낼 수 있는 값 => 문자 개수를 가지고 있는 리스트가 모두 0이면 종료할 거 
            2. DFS 함수를 실행하면서 가져가고 싶은 값! => "여태까지 선택해서 연결된 문자열"
            """
            # 빼고 나서 건네주는거 ok , 그러면 복구를 해줘야지!
            binary_cnt_list[idx] -= 1  # dfs 를 한 루프 돌면 망가져있음.
            dfs(binary_cnt_list, binary_types[idx])
            binary_cnt_list[idx] += 1

    print(f"#{test_case} ")
