import sys

sys.stdin = open('input.txt', 'r')

t = int(input())

for test_case in range(1, t+1):
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))

    for _ in range(m):
        numbers = numbers[1:] + numbers[:1]

    result = numbers[0]

    print(f'#{test_case} {result}')
