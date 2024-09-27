N = int(input())
arr = list(map(int, input().split()))
max_score = max(arr)
total_score = 0
for i in range(N):
    total_score += (arr[i]/max_score) * 100

print(total_score/N)
