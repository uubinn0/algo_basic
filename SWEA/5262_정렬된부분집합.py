'''
필도 코드...................................................
'''

T = int(input())


for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr.pop(0)
    DP = [1 for _ in range(N)]

    for i in range(len(arr)):
        for j in range(i, -1, -1):
            DP[i] = max(DP[i], DP[i - j] + 1 if arr[i - j] < arr[i] else 1)

    print(f'#{tc} {max(DP)}')

