'''
해시문제

해시
탐색 시간복잡도가 O(1)
해시함수를 통해 해당 데이터 저장 위치를 정하고 
이후 해당 데이터를 찾을 때 해당 위치로 바로 이동하여 찾음
'''

import sys
sys.stdin = open('완주하지못한선수.txt', 'r')

T = int(input())

for _ in range(1, T+1):
    par_name = list(map(str, input().split()))
    complete_name = list(map(str, input().split()))

    par_dict = dict()

    # 참가자 명단의 딕셔너리 생성 
    for par_item in par_name:
        if par_item in par_dict.keys():
            par_dict[par_item] += 1
        else:
            par_dict[par_item] = 1

    # print(par_dict)

    # 완주자 명단에 있는 이름은 참가자 명단에서 -1 해줌
    for complete_item in complete_name:
        par_dict[complete_item] -= 1
    
    # 참가자 명단에서 value가 0이 아닌 값을 찾아줌
    for name, value in par_dict.items():
        if value != 0:
            print(name)
            break


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
    