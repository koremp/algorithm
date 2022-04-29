# https://www.acmicpc.net/problem/2798

from sys import stdin

n, m = map(int, stdin.readline().split(' '))
arr = list(map(int, stdin.readline().split(' ')))

x = 0

for i in range(0, n):
  for j in range(i + 1, n):
    for k in range(j + 1, n):
      sum = arr[i] + arr[j] + arr[k]

      if sum <= m:
        x = max(x, sum)

print(x)