# https://www.acmicpc.net/problem/10989
# https://www.acmicpc.net/board/view/26132

from sys import stdin

N = int(stdin.readline())

numbers = [0] * 10001

for _ in range(N):
    numbers[int(stdin.readline())] += 1

for i in range(1, 10001):
    if numbers[i] != 0:
        for _ in range(numbers[i]):
            print(i)
