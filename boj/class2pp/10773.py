# https://www.acmicpc.net/problem/10773

from sys import stdin

N = int(stdin.readline())

counts = []

for _ in range(N):
    counts.append(int(stdin.readline()))

numbers = []

for count in counts:
    if count != 0:
        numbers.append(count)
    else:
        numbers = numbers[:-1]

print(sum(numbers))
