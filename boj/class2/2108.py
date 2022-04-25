# https://www.acmicpc.net/problem/2108

from sys import stdin
from statistics import multimode

n = int(stdin.readline())

arr = [int(stdin.readline()) for _ in range(n)]
arr.sort()

# mean
mean = round(sum(arr) / n)
print(mean)

# middle

if n > 1:
  print(arr[(n // 2)]) 
else:
  print(arr[0])

# most often

mode = multimode(arr)
mode.sort()
print(mode[1] if len(mode) > 1 else mode[0])

# range

print(abs(arr[-1] - arr[0]))