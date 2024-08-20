'''
https://school.programmers.co.kr/learn/courses/30/lessons/43164
'''

import sys
sys.stdin = open('./input/여행경로.txt', 'r')

from collections import deque

T = int(input())


# 인접 리스트로 만들기
def make_dict(arr):
    ticket_dict = dict()

    for ticket_list in arr:
        if ticket_list[0] not in ticket_dict.keys():
            ticket_dict[ticket_list[0]] = [ticket_list[1]]
        elif ticket_list[0] in ticket_dict.keys():
            ticket_dict[ticket_list[0]].append(ticket_list[1])
        
        ticket_dict[ticket_list[0]].sort()
    
    return ticket_dict


def search_track(ticket_dict, start_point, idx, N):
    track_list = list()
    deq = deque([start_point])

    while deq:
        current_airport = deq.popleft()
        track_list.append(current_airport)
        if idx == N: return track_list  # 모든 티켓을 다 사용했다면?
        next_airport = ticket_dict[current_airport][0]
        deq.append(next_airport)    # 다음 공항 추가
        ticket_dict[current_airport].remove(next_airport)   # 방문 체크
        idx += 1


for _ in range(1, 1+T):
    N = int(input())
    tickets = [list(map(str,input().split())) for _ in range(N)]
    # print(tickets)
    start_point = "ICN"

    ticket_dict = make_dict(tickets)
    # print(ticket_dict)

    result = search_track(ticket_dict, start_point, 0, N)

    print(result)

    