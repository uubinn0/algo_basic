import sys
sys.stdin = open('./input/네트워크.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N  = int(input())
    computers = [ list(map(int, input().split())) for _ in range (N)]
    # print(computers)

    graph = dict()
    
