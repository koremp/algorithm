from sys import stdin

for tc in range(int(stdin.readline().rstrip())):
  clothes = {}
  for _ in range(int(stdin.readline().rstrip())):
    name, kind = stdin.readline().rstrip().split()
    clothes[kind] = clothes.get(kind, 0) + 1

  ans = 1
  for count in clothes.values():
    ans *= (count + 1)

  print(ans - 1)
