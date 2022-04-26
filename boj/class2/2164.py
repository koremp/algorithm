# https://www.acmicpc.net/problem/2164
# n = 4
# 1234, 234, 342, 42, 24, 4
# n = 3
# 123, 23, 32, 2
# n = 2
# 12, 2
# deque 는 O(1) 의 시간복잡도를 가지고 있다.

from sys import stdin
from collections import deque

d = deque()

for i in range(int(stdin.readline())):
  d.append(i+1)

while len(d) > 1:
  d.popleft()
  d.append(d.popleft())

print(*d)