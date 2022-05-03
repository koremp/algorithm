# https://www.acmicpc.net/problem/10816

from sys import stdin
from collections import Counter

n = int(stdin.readline())
cards = Counter(map(int, stdin.readline().split(" ")))
n = len(cards)
m = int(stdin.readline())
numbers = list(map(int, stdin.readline().split(" ")))

for num in numbers:
  print(cards[num], end=' ')