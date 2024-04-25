# https://www.acmicpc.net/problem/1074

from sys import stdin

def dim(n, r, c, count):
    if n <= 0:
        return count

    divide = (2 ** (n - 1)) ** 2

    if r < 2 ** (n - 1):
        if c < 2 ** (n - 1):
            return dim(n - 1, r, c, count)
        else:
            return dim(n - 1, r, c - (2 ** (n - 1)), count + divide)
    else:
        if c < 2 ** (n - 1):
            return dim(n - 1, r - (2 ** (n - 1)), c, count + divide * 2)
        else:
            return dim(n - 1, r - (2 ** (n - 1)), c - (2 ** (n - 1)), count + divide * 3)

n, r, c = map(int, stdin.readline().rstrip().split())

print(dim(n = n, r = r, c = c, count = 0))
