'''
https://www.acmicpc.net/problem/1068
'''
from collections import defaultdict

N = int(input())

arr = list(map(int, input().split()))
remove_node = int(input())
tree = defaultdict(list)

# 딕셔너리로 변환
for idx, parent in enumerate(arr):
    # 부모가 없다면 => 루트 노드
    if parent == -1:
        continue

    tree[parent].append(idx)

# print(tree)

# 지울 노드 저장
remove_node_list = []


# 지울 노드 번호 수집
# 지울 노드 + 자식 노드
def remove_child(remove_num):
    # print(f'이번에 지울 노드는 {remove_num}')
    # 지울 노드 리스트에 자신을 추가
    remove_node_list.append(remove_num)

    # 지울 노드에 자식이 있다면
    # print('1. ', tree[remove_num])
    if tree[remove_num]:
        for child_node in tree[remove_num]:
            # 자식 노드에 대해서 반복
            remove_child(child_node)

    return


remove_child(remove_node)
# print(remove_node_list)

for num in remove_node_list:
    # 지울 노드가 부모인 경우 삭제해준다
    if num in tree.keys():
        del tree[num]

print(tree)

# 부모 수
parent_cnt = len(tree.keys())

if parent_cnt != 1:
    # 기존 노드 수에서 지운 노드 수를 제외하고
    # 남은 노드 수에서 부모가 아닌 노드 수 == 리프 노드
    print((N-len(remove_node_list))-parent_cnt)
else:
    print(1)

# 타다닥 타다닥 타다닥 타다닥 타다닥