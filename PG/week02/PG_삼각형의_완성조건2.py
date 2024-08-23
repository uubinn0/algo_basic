def solution(sides):
    num_set = set()
    
    # 남은 한 변이 가장 긴 변인 경우
    for num in range(max(sides),sum(sides)):
        num_set.add(num)
    
    # 이미 있는 변이 가장 긴 변인 경우
    for num in range((max(sides)-min(sides)), max(sides)):
        if min(sides) + num > max(sides):
            num_set.add(num)
    
    answer = len(num_set)
    
    return answer