# https://www.acmicpc.net/problem/1389

from sys import stdin


N, M = map(int, input().split())

relation = [[] for _ in range(N+1)]

for i in range(M):
    A, B = map(int, input().split())
    if A not in relation[B] and B not in relation[A]:
        relation[A].append(B)
        relation[B].append(A)

def BFS(n):
    q = []
    q.append(n)
    visit = [0 for _ in range(N+1)]

    while q:
        c = q.pop(0)
        for i in relation[c]:
            if i != n and not visit[i]:
                q.append(i)
                visit[i] += visit[c] + 1

    return sum(visit)

res=[]

for i in range(1, N+1):
    res.append(BFS(i))


print(res)

print(res[0][0])