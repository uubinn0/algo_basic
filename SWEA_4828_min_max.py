T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    num_list = list(map(int, input().split()))

    max_num, min_num = 0, float('inf')


    # 최대 최소값 찾기
    '''
    리스트를 돌며 각 숫자를 비교함
    현재 저장된 최대값보다 크면 최대값으로 갱신
    현재 저장된 최소값보다 작으면 최소값으로 갱신
    '''
    for num in num_list:
        if num > max_num:
            max_num = num

        if num < min_num:
            min_num = num

    print(f'#{tc} {max_num - min_num}')
