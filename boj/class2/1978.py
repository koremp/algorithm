# https://www.acmicpc.net/problem/1978

from sys import stdin

n = int(stdin.readline())

inputArray = list(map(int, stdin.readline().split(' ')))

count = 0
for i in inputArray:
  e = 0
  if i > 1:
    for o in range(2, i):
      e += 1 if i % o == 0 else 0
    count += 1 if e == 0 else 0
print(count)