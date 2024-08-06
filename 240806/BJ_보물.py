'''
https://www.acmicpc.net/problem/1026

- 0806
합을 작게 만들기 위해서는
가장 큰 수를 작게 만들어야 함
문제에서는 b의 수를 재배열하면 안 된다고 했지만
결국 결과값만 출력하기 때문에 재배열해도 될 듯?
sort하자

a는 오름차순
b는 내림차순
'''

N = int(input())
sum = 0

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

a_list.sort()
b_list.sort(reverse=True)

for i in range(N):
    sum += a_list[i] * b_list[i]

print(sum)