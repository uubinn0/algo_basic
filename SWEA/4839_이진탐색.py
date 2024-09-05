T = int(input())


def search(start, end, target, cnt):
    # 찾은 값
    find_num = int((start+end) / 2)

    # 찾은 값이 찾으려는 값인 경우 끝
    if target == find_num: 
        return cnt

    # 찾으려는 수가 기존에 찾은 수보다 작은 경우 왼쪽으로 범위 축소
    if target < find_num:   
        return search(start, find_num, target, cnt+1)
    # 찾으려는 수가 기존에 찾은 수보다 큰 경우 오른쪽으로 범위 축소
    else:
        return search(find_num, end, target, cnt+1)

    


for tc in range(1, T+1):
    P, A, B = map(int, input().split())

    # 시작 페이지, 끝 페이지, 찾으려는 페이지, 트라이 횟수
    a_cnt = search(1, P, A, 0)
    b_cnt = search(1, P, B, 0)

    if a_cnt < b_cnt:
        result = 'A'
    elif a_cnt > b_cnt:
        result = 'B'
    else:
        result = 0

    print(f'#{tc} {result}')