# https://www.acmicpc.net/problem/1012

from sys import stdin

width, height, k = 0, 0, 0
matrix = [[0 for x in range(51)] for y in range(51)]


def dfs(x, y):
    if y < 0 or y >= height or x < 0 or x >= width or matrix[x][y] == 0:
        return

    matrix[x][y] = 0

    dfs(x, y + 1)
    dfs(x, y - 1)
    dfs(x + 1, y)
    dfs(x - 1, y)


T = int(stdin.readline())

for _ in range(T):
    width, height, k = map(int, stdin.readline().rstrip().split(' '))

    for _ in range(k):
        x, y = map(int, stdin.readline().rstrip().split(' '))
        matrix[x][y] = 1

    count = 0

    for x in range(0, 51):
        for y in range(0, 51):
            if matrix[x][y] == 1:
                dfs(x, y)
                count += 1

    print(count)
