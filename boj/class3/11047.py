import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

min_coin_count = 0

for coin in reversed(coins):
  if coin <= k:
    coin_count = k // coin
    k -= coin_count * coin
    min_coin_count += coin_count

  if k == 0:
    break

print(min_coin_count)