'''
지점을 기준으로 퍼져나가는 형식이니까 BFS로 풀어야할 것 같음
배열의 크기가 어케 되는거지?
동시에 생성이 되는 공간은 어떤 식으로 구현을 해야 할까?
'''

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())