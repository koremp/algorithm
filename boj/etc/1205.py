# boj 1205

from sys import stdin

[n, tae, p] = map(int, stdin.readline().split())

current = []

if n > 0:
    current = list(map(int, stdin.readline().split()))

def solution(n, tae, p, current):
    if n == 0:
        return 1
    else:
       if n == p and current[-1] >= tae:
           return -1
       else:
            for idx, num in enumerate(current):
                if tae >= num:
                    return idx + 1
            return n + 1

print(solution(n, tae, p, current))