'''
https://www.acmicpc.net/problem/1697
수빈이가 있는 지점에서 걸어갈지 순간이동을 할 지 선택
이동하며 curr_sec 증가
동생이 있는 지점에 도착할 때까지 반복
도착한 경우 min_sec 갱신
만약 현재 curr_sec이 min_sec보다 큰 경우 가지치기
'''

N, M = map(int, input().split())
# print(N, M)
min_sec = float('inf')


def dfs(current_pos, current_sec):
    global min_sec

    # 동생을 찾지 못 한 상태인데 시간이 최소 시간보다 큰 경우 애초에 답이 아님
    if current_sec >= min_sec: return

    # 동생이 있는 장소에 도착했다면? 소요 시간 비교하여 갱신 후 종료
    if current_pos == M:
        min_sec = min(min_sec, current_sec)
        return

    # 동생이 있는 곳에 도착하지 못 했다면
    # 위치를 이동하며 수색
    # 위치 이동 방법은 2가지


    # 앞으로 걸어가는 경우
    dfs(current_pos+1, current_sec+1)

    # 뒤로 걸어가는 경우
    # 뒤로 걸었을 때 음수가 아닌 경우에만 이동
    if current_pos -1 >= 0:
        dfs(current_pos-1, current_sec+1)

    # 순간이동 한 경우
    dfs(2*current_pos, current_sec+1)


dfs(current_pos = N, current_sec=0)
print(min_sec)





