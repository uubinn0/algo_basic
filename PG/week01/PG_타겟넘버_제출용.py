'''
https://school.programmers.co.kr/learn/courses/30/lessons/43165
'''

def solution(numbers, target):
    answer = 0
    
    def search_target(idx, total_sum):       
        if idx == len(numbers):
            return 1 if total_sum == target else 0
        
        return (search_target(idx+1, total_sum+numbers[idx])
        + search_target(idx+1, total_sum-numbers[idx]))
    
    answer = search_target(idx=0, total_sum=0)
    
    return answer