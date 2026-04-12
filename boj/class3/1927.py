from sys import stdin
from heapq import heappush, heappop

input = lambda: stdin.readline().rstrip()
n = int(input())

hq = []

for _ in range(n):
    x = int(input())
    if x == 0:
      if len(hq) == 0:
        print(0)
      else:
         print(heappop(hq))
    else:
       heappush(hq, x)
