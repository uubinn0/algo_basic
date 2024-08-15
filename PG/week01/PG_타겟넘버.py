'''
https://school.programmers.co.kr/learn/courses/30/lessons/43165
'''

import sys
sys.stdin = open('타겟넘버_input.txt', 'r')

T = int(input())


def search_target(idx, total_sum):
    global cnt

    # 모든 숫자의 부호를 정했다면
    # 모든 수의 총 합이 target 넘버와 같다면
    # 카운트를 증가시키고 탈출
    if idx == len(numbers):
        if total_sum == target:
            cnt += 1
        return
    
    # 숫자를 양수로 선택한 경우
    search_target(idx+1, total_sum+numbers[idx])

    # 숫자를 음수로 선택한 경우
    search_target(idx+1, total_sum-numbers[idx])


for test_case in range(1, 1+T):
    target = int(input())
    numbers = list(map(int, input().split()))
    cnt = 0

    search_target(idx=0, total_sum=0)

    print(cnt)