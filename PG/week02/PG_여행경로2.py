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
    

def search_path(ticket_dict, idx, N, path):
    path = path[:]
    current_point = path[-1]

    # 탈출 조건
    if idx == N:
        # print(path)
        return path

    # 자식노드가 있는 경우
    # 현재 노드가 출발지인 티켓이 있고 자식 노드가 남아있는 경우
    # 조건문 평가 순서 때문에 키 값이 있는지 먼저 확인해야 에러가 나지 않음
    if current_point in ticket_dict.keys() and ticket_dict[current_point]:
        for next_point in ticket_dict[current_point]:
            # 자식노드를 다음 경로로 선택한 경우
            temp_dict = copy.deepcopy(ticket_dict)

            # 방문표시처럼 해당 자식 노드를 인접 리스트에서 제거
            # 다음에 노드들을 돌 때 해당 노드로 돌아오지 않도록 함
            temp_dict[current_point].remove(next_point) 
            path.append(next_point) # 결과 경로 값 리스트에 다음 노드 추가
            result = search_path(temp_dict, idx+1, N, path)

            if result:
                return result

            # 방문처리했던 것들 다시 원상복구
            path.pop()

    # 자식 노드가 없는 노드인 경우 이전 노드로 돌아가기
    else:
        return
    
def solution(tickets):
    N = len(tickets)
    start_point = "ICN"
    
    ticket_dict = make_dict(tickets)
    
    # 시작지점이 이미 들어있는 리스트
    # 이후에 결과로 반환할 예정
    path = [start_point]
    result = search_path(ticket_dict, 0, N, path)
    # print(result)
    return result

solution([["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"], ["BOO", "DOO"]])