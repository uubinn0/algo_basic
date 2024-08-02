import sys

sys.stdin = open('4834_input.txt', 'r')

T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    num_list = list(map(int, input()))
    # print(num_list, cnt_list)

    # 딕셔너리를 만들어서
    # 키 값으로 접근해서 value를 증가시키자
    num_dict ={}
    for i in num_list:
        num_dict[i] = 0

    for i in num_list:
        num_dict[i] += 1
    
    print(num_dict)

    
    