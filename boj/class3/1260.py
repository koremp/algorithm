from collections import deque
from sys import stdin

N, M, V = map(int, stdin.readline().rstrip().split())

graph = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, stdin.readline().rstrip().split())
    graph[a][b] = graph[b][a] = 1

visited1 = [0]*(N+1)
visited2 = [0]*(N+1)

def dfs(v):
    visited1[v] = 1
    print(v, end=' ')
    for i in range(1, N+1):
        if graph[v][i] == 1 and visited1[i] == 0:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited2[v] = 1
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for i in range(1, N+1):
            if graph[node][i] == 1 and visited2[i] == 0:
                queue.append(i)
                visited2[i] = 1

dfs(V)
print()
bfs(V)
