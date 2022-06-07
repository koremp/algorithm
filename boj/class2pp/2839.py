# https://www.acmicpc.net/problem/2839

from sys import stdin

n = int(stdin.readline())


cnt = 0
while n > 0:
    if n % 5 == 0:
        n -= 5
        cnt += 1
    elif n % 3 == 0:
        n -= 3
        cnt += 1
    elif n > 5:
        n -= 5
        cnt += 1
    else:
        cnt = -1
        break

print(cnt)
