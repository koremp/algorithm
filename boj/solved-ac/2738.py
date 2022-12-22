import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

result = []

for i in range(n):
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    result.append(a)

for i in range(n):
    b = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(len(b)):
        result[i][j] += b[j]

for i in range(n):
    print(*result[i])