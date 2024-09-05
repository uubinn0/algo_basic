'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZC_w6Z6yygDFAQW&contestProbId=AZGv4enKpNkDFAXd&probBoxId=AZGv3Un6pMkDFAXd&type=USER&problemBoxTitle=4w_homework&problemBoxCnt=5
'''

T = int(input())


def make_hash(txt):
    N = len(txt)
    K = 256

    hash_num = 0

    for i in range(N):
        hash_num += ord(txt[i]) * (K**(N-1-i))
    return hash_num



for tc in range(1, T+1):
    pattern = str(input())
    text = str(input())
    result = 0
    cnt = 0 # 일치 문자 수를 체크

    # 패턴의 해시값
    patrn_hash = make_hash(pattern)
    
    N = len(pattern)

    # 롤링 해시 기법 쓰고 싶지만 너무 귀찮음
    for i in range(0, len(text)-N+1):
        # print(text[i:i+N])

        # 자리마다의 해시값 계산    
        text_hash = make_hash(text[i:i+N])

        # 해시값이 패턴과 같을 때 두 문자열을 비교하기
        if text_hash == patrn_hash:
            # print(f'hash ; {text_hash} {patrn_hash}')
            txt = text[i:i+N]

            # 문자를 바로 비교하기
            if txt == pattern:
                result = 1


            # # print(txt, pattern)
            # for j in range(N):
            #     # 서로 비교하여 각 자리 문자가 같은 경우
            #     if txt[j] == pattern[j]:
            #         # print(text[j], pattern[j])
            #         cnt +=1

    # print(cnt, N)   
    # if cnt == N :
    #     result = 1

    print(f'#{tc} {result}')