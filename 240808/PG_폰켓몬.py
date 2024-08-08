import sys
sys.stdin = open('폰켓몬_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    nums = list(map(int, input().split()))
    select_cnt = len(nums) //2

    num_set_len = len(set(nums))

    if num_set_len > select_cnt:
        print(select_cnt)
    elif num_set_len == select_cnt:
        print(select_cnt)
    elif num_set_len < select_cnt:
        print(num_set_len)