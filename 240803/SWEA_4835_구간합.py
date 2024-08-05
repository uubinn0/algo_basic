'''
계속 같은 걸 반복하니까 dfs를 쓸 수 있을 거 같음
반복 : 각 숫자 별로 인접 값의 합을 구함
      구한 합이 저장된 최고 합보다 작은지 비교 후 교체
예외 : 첫 번째 인덱스의 경우 idx-1 값이 없음 / 마지막 값의 경우 idx+1이 없음
'''

T = int(input())

for test_case in range(1, T+1):
    # 숫자 수 N , 합을 구할 숫자 수 M
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))

    min_sum, max_sum = float('inf'), 0  # 최소 합을 담을 변수


    for idx in range(0, N+1-M):
        temp_sum = 0    # 임시 합   for문 안에서만 쓰는 변수니까 for문 안에서 선언하자
        for m in range(M):
            temp_sum += num_list[idx+m]    

        if temp_sum < min_sum:
            min_sum = temp_sum

        if temp_sum > max_sum:
            max_sum = temp_sum

    print(f'#{test_case} {max_sum-min_sum}')