import sys 
import math
sys.stdin = open('양팔저울_input.txt', 'r')

T = int(input())


def find_way(idx, left, right):
    global result
    global check

    if left < right:    # 왼쪽이 오른쪽보다 작아지는 순간이 생기면 바로 탈출
        return
    
    if left >= total_weight // 2:   # 현재 왼쪽 무게가 전체 무게의 절반 이상이면
        # 현재 남은 추를 어떤 순서로 어디에 놓아도 모든 경우가 왼쪽이 더 무겁다
        # 따라서 남은 추의 경우의 수만 구하고 더해준다
        result += (2**(N-idx)) * math.factorial(N-idx)
        return

    if idx == N:    # 모든 추를 다 올렸다면 가능한 경우의 수라는 뜻이니까 
        result += 1 # result 증가 후 종료
        return
    
    for current_select in range(len(weight)):
        # 현재 고른 추가 올리지 않은 추인 경우에만
        if not check[current_select]:
            # 추 사용했음을 체크
            check[current_select] = True
            # 해당 추를 왼쪽에 올리기
            find_way(idx+1, left+weight[current_select], right)
            # 해당 추를 오른쪽에 올리기
            find_way(idx+1, left, right+weight[current_select])
            # 추 사용 끝났음 체크
            check[current_select] = False

        else: continue  # 이미 사용한 추인 경우 넘어감


for test_case in range(1, T+1):
    N = int(input())
    weight  = list(map(int, input().split()))
    # print(weight)
    result = 0
    check = [False] * N
    total_weight = sum(weight)  # 추의 전체 무게

    for first_select in range(len(weight)):
        check[first_select] = True
        find_way(idx=1, left = weight[first_select], right = 0)
        check [first_select] = False

    
    print(result)
