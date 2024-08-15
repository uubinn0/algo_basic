'''
https://school.programmers.co.kr/learn/courses/30/lessons/1844
'''

from collections import deque
import copy
dyx = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def solution(maps):
    
    def search(y, x, cnt, visited):
        Y = len(visited)
        X = len(visited[0])
        
        # # 도착 지점 주변이 막힌 경우 - 가지치기하고 싶은데 이거 넣으면 사이트에서 오류남 엌ㅋㅋ
        # # 생각하기 귀찮으니까 일단 뺌
        # if visited[X-1][Y-2] == 0 and visited[X-2][Y-1] == 0:
        #     return -1
        
        deq = deque([(y, x, 1)])
        visited[y][x] = 2
        
        while deq:
            y, x, cnt= deq.popleft()

            # 도착 지점이면?
            if y == Y-1 and x == X-1:
                return cnt

            for i, j in dyx:
                # 새 좌표
                new_y = y + i
                new_x = x + j

                # out of range
                if new_x < 0 or new_y < 0 or new_x >= X or new_y >= Y:
                    continue

                # 벽인 경우
                if visited[new_y][new_x] == 0:
                    continue

                # 방문한 곳인 경우
                if visited[new_y][new_x] == 2:
                    continue

                # 갈 수 있는 좌표라면
                deq.append((new_y, new_x, cnt+1))  # 큐에 넣고
                visited[new_y][new_x] = 2   # 방문 처리
                
        return -1
    
    answer = search(y=0, x=0, cnt=0, visited=maps)
    
    return answer