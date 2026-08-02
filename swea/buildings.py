import sys

sys.stdin = open('input.txt', 'r')

t = 10

for test_case in range(1, t+1):
    n = int(input())
    buildings = list(map(int, input().split()))

    view_count = 0
    for i in range(2,n-2):
        current = buildings[i]
        near_buildings = [buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2]]

        if current > max(near_buildings):
            view_count += (current - max(near_buildings))

    print(f'#{test_case} {view_count}')
