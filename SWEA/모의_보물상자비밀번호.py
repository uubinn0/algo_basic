import sys
sys.stdin = open('./input/보물상자_input.txt', 'r')

from collections import deque
T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    pw = str(input())
    pw_q = deque([pw[i] for i in range(N)])
    # print(pw_q)
    num_cnt = N //4 # 한 변에 있는 숫자 수
    pw_set = set()  # 중복되는 숫자는 세지 않는다

    for i in range(num_cnt):
        pw_q.rotate(1)  
        temp_list = list(pw_q)
        for j in range(0,N,num_cnt):
            temp_str = ''.join(temp_list[j:j+num_cnt])
            # print(temp_str)
            # print(int(temp_str, 16))
            pw_set.add(int(temp_str, 16)) # 슬라이싱한 문자열을 10진수로 바꾸고 리스트에 추가

    pw_list = list(pw_set)
    pw_list.sort(reverse=True)

    # print(pw_list)
    print(f'#{tc} {pw_list[K-1]}')
            




