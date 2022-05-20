# https://www.acmicpc.net/problem/2775

from sys import stdin

T = int(stdin.readline())

for i in range(T):
    k = int(stdin.readline())  # 층
    n = int(stdin.readline())  # 호

    a = [[1] * 14 for _ in range(k + 1)]
    for i in range(1, n):
        a[0][i] = i
    for j in range(1, k + 1):
        for u in range(n + 1):
            if u != 0:
                a[j][u] = a[j - 1][u] + a[j][u - 1]
    print(a[k][n - 1])
