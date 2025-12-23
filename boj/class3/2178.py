from collections import deque
from sys import stdin

N, M = map(int, stdin.readline().rstrip().split())

graph = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(N):
    graph.append(list(map(int, stdin.readline().rstrip())))

def bfs(x, y):
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[N-1][M-1]

print(bfs(0,0))
