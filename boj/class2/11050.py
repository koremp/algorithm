# https://www.acmicpc.net/problem/11050

from sys import stdin


def fact(n):
    if n == 0:
        return 1
    a = 1
    for i in range(1, n + 1):
        a *= i

    return a


n, k = map(int, stdin.readline().split())

print(fact(n) // (fact(k) * fact(n - k)))
