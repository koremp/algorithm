from sys import stdin

n, m = map(int, stdin.readline().rstrip().split())

names = {}
indexes= {}

for i in range(1, n + 1):
  name = stdin.readline().rstrip()
  names[i] = name
  indexes[name] = i

for _ in range(m):
  entry = stdin.readline().rstrip()
  if entry.isdecimal():
    print(names[int(entry)])
  else:
    print(indexes[entry])