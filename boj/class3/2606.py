from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)

def bfs(start):
    q = deque([start])
    visited[start] = True
    infected = 0

    while q:
        v = q.popleft()
        for nxt in graph[v]:
            if not visited[nxt]:
                visited[nxt] = True
                infected += 1
                q.append(nxt)
    return infected

print(bfs(1))