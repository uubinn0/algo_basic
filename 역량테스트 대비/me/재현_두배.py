'''
N개의 수열이 주워진다.
A라는 수열이 있을 때 각 수열의 수는 아래와 같이 변경이 딱 한 번 가능하다
A[i] = max(A[i] + i, i) => i는 1부터 시작

수열의 합이 2N 이상이 되도록 하기 위해 최소 변경 횟수를 구하시오.
-----
11번부터 터짐
N이 굉장히 큰 수까지 주워졌던 거 같음 10만?
python 50개 30초
'''
def search(idx, nums, is_change):
    global min_work
    # print(nums)

    # 2배 이상이 되었다면 현재까지의 작업 횟수 비교
    if sum(nums) >= 2*N:
        # print('here')
        min_work = min(min_work, is_change.count(True))
        return

    # 모든 수를 다 돈 경우
    if idx >= N:
        return

    # 변경이 가능한 숫자면
    if not is_change[idx]:
        temp = nums[idx]
        nums[idx] = max(nums[idx] + (idx+1), (idx+1))
        is_change[idx] = True
        # print('->', nums)
        search(idx+1, nums, is_change)
        is_change[idx] = False
        nums[idx] = temp

    # 못 바꾸는 놈이면 걍 넘어감
    search(idx+1, nums, is_change)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    min_work = 0

    # 처음부터 수열의 합이 2N인 경우에는 작업을 하지 않음
    if sum(A) < 2*N:
        visited = [False] * N
        min_work = float('inf')
        search(0, A, visited)

    print(f'#{tc} {min_work}')


