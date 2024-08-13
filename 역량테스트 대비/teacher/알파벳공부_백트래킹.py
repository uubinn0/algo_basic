import sys
sys.stdin = open('sample_input.txt')


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    words = [input().strip() for _ in range(N)]
    word_sets = [set(word) for word in words]
    # word_sets = [set(input().strip()) for _ in range(N)]
    word_set_cnt = 0


    # detph: 선택할지, 말지 결정하려는 값의 인덱스
    # current_set : 여태까지 선택해온 집합
    def dfs(depth, current_set):
        global word_set_cnt

        if depth == len(word_sets):
            if len(current_set) == 26:
                word_set_cnt += 1
            return

        # depth 에 해당하는 단어를 선택한 경우
        # | => 파이썬에서 합집합
        dfs(depth + 1, current_set | word_sets[depth])
        # depth 에 해당하는 단어를 선택하지 않은 경우
        dfs(depth + 1, current_set)


    """
    DFS 라는게 결국 재귀호출이다. 
    파라미터를 뭐로 써야할까? => 내가 모르겠다.. 그러면 위에서 나온 변수 다 집어넣자
    1. 현재 재귀호출을 끝낼 수 있는 파라미터  => 
    2. 우리가 누적해서 가져가고 싶은 값 (파라미터) => 만들어낸 단어 집합
    """
    dfs(0, set())

    print(f"#{t} {word_set_cnt}")
