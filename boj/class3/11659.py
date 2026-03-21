from sys import stdin

n, m = map(int, stdin.readline().rstrip().split())

li = []

li = list(map(int, stdin.readline().rstrip().split()))

value_li = [0 * (len(li) + 1)]
for i in range(len(li)):
  value_li.append(li[i] + value_li[i])

for _ in range(m):
  i, j = map(int, stdin.readline().rstrip().split())
  print(value_li[j] - value_li[i - 1])
