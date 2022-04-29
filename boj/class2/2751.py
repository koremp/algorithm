# https://www.acmicpc.net/problem/2751

from sys import stdin

n = int(stdin.readline())

lst = [int(stdin.readline()) for _ in range(n)]
lst.sort()

for i in lst:
    print(i)