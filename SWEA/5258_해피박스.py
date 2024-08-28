'''
DP 기초 knapack 문제
배열 초기화 부분이 핵심
현재 넣으려는 물건을 넣기 위해서는 
이전에 구한 해에서 
현재 넣으려는 물건의 무게만큼 빼줬을 때의 상자의 가치 + 현재 넣으려는 물건의 가치를 합한 값과
이전에 구했던 해와 비교해서 더 큰 값을 최적해로 채택함
'''

# from pprint import pprint

T = int(input())

for tc in range(1, T+1):
    box_size, item_cnt = map(int, input().split())
    item = [list(map(int, input().split())) for _ in range(item_cnt)]
    # pprint(item)

    # 2차원 배열 만들기
    dp = [[ 0 for _  in range(box_size +1)] for _ in range(item_cnt+1)]

    # dp 배열 초기화 하기
    # 1부터 시작하는 이유 : 
    # box_idx(아무 가방도 없는 경우)가 0인 경우 모두 0, max_size(최대 담을 수 있는 사이즈가 0인 경우)가 0인 경우도 모두 0의 값을 가진다.
    for box_idx in range(1, item_cnt+1):
        for max_size in range(1, box_size+1):
            # 담을 물건의 크기가 현재 담을 수 있는 크기보다 큰 경우
            if item[box_idx-1][0] > max_size:
                dp[box_idx][max_size] = dp[box_idx-1][max_size]
            else:
                dp[box_idx][max_size] = max(dp[box_idx-1][max_size-item[box_idx-1][0]] + item[box_idx-1][1], dp[box_idx-1][max_size])

            # pprint(dp) 
    
    # pprint(dp)
    result = dp[-1][-1]
    print(f'#{tc} {result}')