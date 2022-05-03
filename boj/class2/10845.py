# https://www.acmicpc.net/problem/10845

from sys import stdin
from collections import deque

result = []
queue = deque([])
for _ in range(int(stdin.readline().strip())):
    data = stdin.readline().strip()
    if "push" in data:
        queue.append(int(data[5:]))
    elif "pop" in data:
        if len(queue) >= 1:
            result.append(queue.popleft())
        else:
            result.append(-1)
    elif "size" in data:
        result.append(len(queue))
    elif "empty" in data:
        if len(queue) >= 1:
            result.append(0)
        else:
            result.append(1)
    elif "front" in data:
        if len(queue) >= 1:
            result.append(queue[0])
        else:
            result.append(-1)
    elif "back" in data:
        if len(queue) >= 1:
            result.append(queue[-1])
        else:
            result.append(-1)

for x in result:
    print(x)
