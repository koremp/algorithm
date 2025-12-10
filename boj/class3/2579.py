from sys import stdin

n = int(stdin.readline().rstrip())
stairs = [0] + [int(stdin.readline().rstrip()) for _ in range(n)]

if n == 1:
  print(stairs[1])
  exit()

dp = [0] * (n + 1)
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]

for i in range(3, n + 1):
  dp[i] = max(
    dp[i - 2] + stairs[i],
    dp[i - 3] + stairs[i - 1] + stairs[i],
  )

print(dp[n])