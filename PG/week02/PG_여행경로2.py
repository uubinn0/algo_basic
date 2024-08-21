'''
개꼴아박음ㅋㅋ
걍 다 지우고 새로 시작하자....

그냥 순환하는지 먼저 체크하고 적합하면 dfs를 도는게 나을 거 같음
순환 체크... 
'''
import copy

def make_dict(arr):
    ticket_dict = dict()

    for ticket_list in arr:
        if ticket_list[0] not in ticket_dict.keys():
            ticket_dict[ticket_list[0]] = [ticket_list[1]]
        elif ticket_list[0] in ticket_dict.keys():
            ticket_dict[ticket_list[0]].append(ticket_list[1])
        
        ticket_dict[ticket_list[0]].sort()
    
    return ticket_dict


def check_cycle(ticket_dict, start_point, next_point):
    if (next_point in ticket_dict[start_point]) and (start_point in ticket_dict[next_point]):
        return True
    else:
        return False
    

def search_path(ticket_dict, current_point, idx, N, path):
    



def solution(tickets):
    N = len(tickets)
    start_point = "ICN"
    
    ticket_dict = make_dict(tickets)
    
    result = search_path(ticket_dict, start_point, 0, N, [])
     
    return result