import sys
import math
sys.stdin = open("sample_input (1).txt", "r")

T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())  # 추의 개수
    arr = list(map(int, input().split()))  # 추의 무게
    result = 0

    total_w = sum(arr)
    def dfs(depth, l_sum, r_sum):
        global result

        # 오른쪽 저울의 무게가 왼쪽 저울의 무게보다 무거우면 안된다.
        if l_sum < r_sum:
            return

        # 왼쪽이 총 무게의 절반보다 크거나 같으면
        # 사실 아무렇게 놔도 된다.
        if l_sum >= total_w / 2:
            # 남은 추에서 만들 수 있는 모든 경우의수
            # N - depth => 남은 추의 개수
            # 2^N * N!
            result += (2 ** (N-depth)) * math.factorial(N - depth)
            return

        # if depth == N:
        #     # 순열 개수만큼 추가재주는 로직을 넣어야해요.
        #     return

        for i in range(N):
            if visited[i]: continue
            visited[i] = True
            # 왼쪽 저울에 추를 올려놓는 경우
            dfs(depth + 1, l_sum + arr[i], r_sum)

            # 오른쪽 저울에 추를 올려놓는 경우
            dfs(depth + 1, l_sum, r_sum + arr[i])
            visited[i] = False


    visited = [False] * N
    """
    dfs 파라미터 뭐로할까?
    부분집합 문제다..
    1. 재귀호출을 중단할 파라미터 => 해당 추를 선택할거냐, 안할거냐를 가리키는 인덱스 (depth) 
    2. 누적해서 가져가고 싶은 파라미터 => 추의 무게를 가져가고 싶다. 
    그 수를 선택하냐, 안하냐의 문제였다. ( 그래서 하나의 수 값만 파라미터 보내면 됐다. )
    왼쪽에 놓냐, 오른쪽에 놓냐? 
    """
    for n in range(N):
        visited[n] = True
        dfs(1, arr[n], 0)
        visited[n] = False

    # dfs(0, 0, 0)
    print(f"#{test_case} {result}")
