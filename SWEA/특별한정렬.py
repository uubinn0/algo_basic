'''
선택 정렬로 가장 큰 숫자, 가장 작은 숫자를 찾음
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N-1):
        min_idx = i
        max_idx = i
        if i % 2 == 0:  # 큰 수를 찾아야 하는 경우
            for j in range(i+1, N):
                # 기존 값과 새 값 중 새 값이 더 큰 경우
                if arr[max_idx] < arr[j]:
                    max_idx = j

            arr[i], arr[max_idx] = arr[max_idx], arr[i]

        else:   # 작은 수를 찾아야 하는 경우
            for j in range(i + 1, N):
                # 기존 값과 새 값 중 새 값이 더 작은 경우
                if arr[min_idx] > arr[j]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]


    print(f'#{tc}', *arr[:10])

