from sys import stdin

T = int(stdin.readline().rstrip())

n_list = [int(stdin.readline().rstrip()) for _ in range(T)]

dp = [0,
      1, 2, 4, 0, 0,
      0, 0, 0, 0, 0,
      0]

for i in range(4, 11):
  dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

for n in n_list:
  print(dp[n])





