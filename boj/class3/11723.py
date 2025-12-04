from sys import stdin

M = int(stdin.readline().rstrip())

S = set()


for _ in range(M):
  entry = stdin.readline().rstrip().split(' ')

  if len(entry) == 1:
    if entry[0] == 'all':
      S = set(i for i in range(1, 21))
    else:
      S = set()
  else:
    operation, num  = entry[0], int(entry[1])
    if operation == 'add':
      S.add(num)
    elif operation == 'remove':
      S.discard(num)
    elif operation == 'check':
      print(1 if num in S else 0)
    else:
      if num in S:
        S.discard(num)
      else:
        S.add(num)


