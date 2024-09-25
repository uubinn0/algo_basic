T = int(input())

for _ in range(T):
    N, txt = map(str, input().split())
    # print(N, txt)

    N = int(N)
    result = ''

    for char in txt:
        result += char*N

    print(result)