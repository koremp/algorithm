# https://www.acmicpc.net/problem/1676

from sys import stdin

T = int(stdin.readline())

fac = 1

for i in range(T):
    fac = fac * (i + 1)

strFac = str(fac)

result = 0

for char in reversed(strFac):
    if char == '0':
        result = result + 1
    else:
        break

print(result)