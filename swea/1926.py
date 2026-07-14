n = int(input())
for i in range(1, n+1):
  if '3' in str(i) or '6' in str(i) or '9' in str(i):
    for c in str(i):
      if c == '3' or c == '6' or c == '9':
        print('-', end='')
    print(end=' ')
  else:
    print(i, end=' ')