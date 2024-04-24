# https://www.acmicpc.net/problem/18110

from sys import stdin

def roundUp(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

N = int(stdin.readline())

levels = []

for _ in range(N):
    level = int(stdin.readline())
    levels.append(level)

if N == 0:
    print(0)

elif N == 1:
    print(sum(levels))

else:
    delete = roundUp(N * 0.15)
    levels.sort()
    levels = levels[delete:N - delete]
    print(len(levels))
    print(N - delete * 2)
    # result = roundUp(sum(levels) / len(levels))
    result = roundUp(sum(levels) / (N - delete * 2))
    print(result)