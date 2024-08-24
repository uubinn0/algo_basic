'''
https://school.programmers.co.kr/learn/courses/30/lessons/12906
'''

def solution(arr):
    answer = [arr[0]]

    for i in range(1,len(arr)):
        pre_num = answer.pop()  # 스택에 있던 숫자를 뺌
        # 스택에 있던 숫자와 그 다음 숫자가 같은지 확인
        # 만약 같다면 스택에 있던 숫자는 제거하고 현재 숫자를 넣음
        if pre_num == arr[i]:   
            answer.append(arr[i])  # 스택에 숫자 넣음
        # 다른 경우엔 두 숫자 모두 넣어줌
        else:
            # 순서를 위해 pre_num 먼저 삽입
            answer.append(pre_num)
            answer.append(arr[i])
    
    return answer

solution([1,1,3,3,0,1,1])
