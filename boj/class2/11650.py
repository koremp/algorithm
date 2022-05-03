# https://www.acmicpc.net/problem/11650

from sys import stdin

n = int(stdin.readline())
xy_list = []

for i in range(n):
    x, y = map(int, stdin.readline().split())
    xy_list.append([x, y])

xy_list.sort(key=lambda row: (row[0], row[1]))

for i in range(n):
    print(xy_list[i][0], xy_list[i][1])
