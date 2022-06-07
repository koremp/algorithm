# https://www.acmicpc.net/problem/11651

from sys import stdin

N = int(stdin.readline())

axis_dict = {}

for _ in range(N):
    x, y = map(int, stdin.readline().split(" "))

    if axis_dict.get(y):
        axis_dict[y].append(x)
    else:
        axis_dict[y] = [x]

for i in sorted(axis_dict.keys()):
    for j in sorted(axis_dict[i]):
        print(j, i)
