import sys
import math

input = sys.stdin.readline

def solve():
  mn, mx = map(int, input().split())
  n = mx - mn + 1
  marked = [False] * n

  limit = math.isqrt(mx)
  for i in range(2, limit + 1):
    sq = i * i
    start = ((mn + sq - 1) // sq) * sq

    for x in range(start, mx + 1, sq):
      marked[x - mn] = True

    print(n - sum(marked))

if __name__ == "__main__":
  solve()
