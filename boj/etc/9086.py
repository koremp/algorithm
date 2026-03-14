from sys import stdin

for _ in range(int(stdin.readline().rstrip())):
  s = stdin.readline().rstrip()
  first = s[0]
  last = s[len(s) - 1]
  print(f'{first}{last}')