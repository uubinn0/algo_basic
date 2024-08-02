# 평균 시간 복잡도 O(N)
# 최악의 시간 복잡도 O(N^2) - 해시 테이블이 작동하지 않을꼉우

import sys

sys.stdin = open('4834_input.txt', 'r')

T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    num_list = list(map(int, input())) #[4, 9, 6, 7, 9]
    num_set = set(num_list)

    max_num = -1
    max_cnt = 0

    num_dict = dict()
    for num in num_list:
        # 숫자 리스트를 돌며 각 숫자의 빈도수를 딕셔너리에 저장
        # key: 숫자 value: 빈도수
        if num not in num_dict:
            # 리스트의 숫자가 딕셔너리에 없는 경우 value를 1로 변경
            num_dict[num] = 1
        elif num in num_dict:
            # 리스트의 숫자가 이미 딕셔너리에 있는 경우 value에 1을 증가시켜줌
            num_dict[num] += 1

    # 딕셔너리 키값을 순회함
    for key in num_dict.keys():
        if max_cnt <= num_dict.get(key) and max_num < key:
            # 만약 기존 최대 빈도수보다 큰 value를 가지고 있으며
            # 최대 숫자 보다 key값도 큰 경우에
            # 각 값을 갱신해줌
            max_cnt = num_dict.get(key)
            max_num = key


    # print(max(num_dict.values()))
    
    print(f'#{tc} {max_num} {max_cnt}')