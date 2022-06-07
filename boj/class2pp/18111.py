# https://www.acmicpc.net/problem/18111
# https://www.acmicpc.net/board/view/79610

import sys

input = sys.stdin.readline
n, m, b = map(int, input().split())
temp = 0
tmp = []
arr = []
mini = 100000000
height = 0
for i in range(n):
    tmp = map(int, input().split())
    arr += tmp

maxx = int((sum(arr) + b) / (n * m))
for ii in range(maxx + 1):
    for i in arr:
        if i < ii:
            temp += ii - i
        elif i > ii:
            temp += (i - ii) * 2
    if temp <= mini:
        mini = temp
        height = ii
    temp = 0

print(mini, height)
