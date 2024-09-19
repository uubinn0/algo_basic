'''
티셔츠는 남아도 괜찮음
볼펜은 남으면 안 됨
'''

N = int(input())
t_arr = list(map(int,input().split()))
T, P = map(int, input().split())
pen_bunch = 0
pen = 0
t_bunch = 0

# 티셔츠
for item in t_arr:
    if item == 0:
        continue

    if T > item:
        t_bunch += 1
    else:
        # 묶음으로 나눠지면
        if item % T == 0:
            t_bunch += (item // T)
        # 나눠지지 않으면
        else:
            t_bunch += (item // T) + 1

print(t_bunch)

# 펜
# 나눠지면
if N % P == 0:
    pen_bunch = N//P
# 나눠지지 않으면
else:
    pen_bunch = N//P
    pen = N % P

print(pen_bunch, pen)



