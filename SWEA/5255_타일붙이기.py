T = int(input())

for tc in range(1, T+1):
    N = int(input())

    DP = [0 for _ in range(N+1)]

    DP[1] = 1
    DP[2] = 3
    DP[3] = 6

    for i in range(4, N+1):
        DP[i] = DP[i-1] + 2*DP[i-2] + DP[i-3]

    print(DP[-1])

