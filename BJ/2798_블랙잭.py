from itertools import combinations

N, target_num = map(int, input().split())
card = list(map(int, input().split()))
max_num = 0
for card_select in combinations(card, 3):
    if sum(card_select) <= target_num and sum(card_select) > max_num:
        max_num = sum(card_select)

print(max_num)