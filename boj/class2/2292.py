# https://www.acmicpc.net/problem/2292

from sys import stdin

num = int(stdin.readline())
res = 0
k = 1
li = []
for i in range(0, num):
    k += i * 6
    li.append(k)
    if num > li[i]:
        res += 1
    else:
        res += 1
        break
    
print(res)