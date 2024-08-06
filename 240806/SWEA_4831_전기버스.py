'''
- 0806
for문을 정류장 수 만큼 돌면서 이동
흠... for문이 아니라 이동 가능 거리가 0이 아닐 때까지 돌리는게 나을지도? 
=> 이 경우 현재 위치를 나타낼 인덱스 변수가 필요함
=> 마지막에 현재 인덱스와 최종 도착해야 하는 정류장의 인덱스가 같으면 도착한 것
=> 다르다면 도착하지 못한 것

현재 위치의 정류장에 충전소가 있는 경우

다음 충전소가 있는 정류장까지의 거리를 구하고

해당 거리가 현재 남은 이동 가능 거리보다 작거나 같은 경우
충전을 하지 않고 이동 

해당 거리가 현재 남은 이동 가능 거리보다 큰 경우
현재 충전소에서 충전 후 이동

'''

T = int(input())

for test_case in range(1, T+1):
    max_move, station, charge_station = map(int, input().split())
    charge_list = list(map(int, input().split()))
    # print(max_move, station, charge_station)
    # print(charge_list)
    currnet_idx = 0
    move_cnt = max_move # 이동 가능 거리
    charge_cnt = 0  # 충전 횟수

    while move_cnt > 0 or currnet_idx == station:
        currnet_idx += 1    # 한 칸 이동
        move_cnt -= 1   # 이동 가능 거리 감소
        print(currnet_idx, move_cnt)
        # 현재 위치에 충전기가 있다면
        if currnet_idx in charge_list:
            # 다음 충전기 위치까지의 거리를 구하기
            next_charge_idx = charge_list.index(currnet_idx) + 1
            print('다음 충전기 인덱스', next_charge_idx)
            print('다음 충전기 위치 정류장', charge_list[next_charge_idx])

            # 그 거리가 현재 이동 가능한 거리보다 작거나 같은 경우
            # 다음 충전소에서 충전하는 것이 이득임
            if charge_list[next_charge_idx] - currnet_idx <= move_cnt:
                # 충전하지 않고 그냥 pass
                print('pass')
                continue
            # 거리가 현재 이동 가능한 거리보다 큰 경우
            # 다음 충전소에 도착하기 전에 이동 횟수가 0이 됨
            # 따라서 현재 충전소에서 충전을 해야함
            elif next_charge_idx - currnet_idx > move_cnt:
                # 이동 가능 거리 충전
                move_cnt = max_move
                # 충전 횟수 증가
                charge_cnt += 1
                print(f'충전함 {move_cnt}, {charge_cnt}')

        
    if currnet_idx != station:
        charge_cnt = -1

    print(f'#{charge_cnt}')




