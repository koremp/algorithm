# https://www.acmicpc.net/problem/11866

from sys import stdin

from collections import deque

n, k = map(int, stdin.readline().split())

cnt = 0
queue = deque()
answer = []
for i in range(1, n + 1):
    queue.append(i)
while queue:
    cnt += 1
    if k == cnt:
        answer.append(str(queue.popleft()))
        cnt = 0
    else:
        queue.append(queue.popleft())

print("<", end="")
for number in answer:
    if number == answer[-1]:
        print(number, end="")
    else:
        print(number, end=", ")

print(">")
