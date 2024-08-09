import sys
sys.stdin = open('완주하지못한선수.txt', 'r')

T = int(input())

for _ in range(1, T+1):
    par_name = list(map(str, input().split()))
    complete_name = list(map(str, input().split()))

    par_set = set(par_name)
    complete_set = set(complete_name)

    if len(par_set) != len(par_name):
        # 동명이인이 있다
        pass
    else:
        last_name = par_set - complete_set
        print(last_name.pop())



    '''
    par_name = list(map(str, input().split()))
    complete_name = list(map(str, input().split()))

    for par in par_name:
        if par not in complete_name:
            print(par)
            break
        else:
            # 동명이인처리를 위해 검사 후 완주자 리스트에서 해당 이름을 제거
            complete_name.remove(par)
            continue
    '''
    