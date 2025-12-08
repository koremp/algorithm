import sys
input = sys.stdin.readline

n, m = map(int, input().split())

not_heard = set(input().strip() for _ in range(n))
not_seen = set(input().strip() for _ in range(m))

answer = sorted(not_heard & not_seen)

print(len(answer))
for name in answer:
    print(name)
