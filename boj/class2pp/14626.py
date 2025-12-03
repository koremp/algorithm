from sys import stdin

isbn = list(stdin.readline().strip())

sum = 0

injured_idx = -1

for idx, val in enumerate(isbn[0:13]):
  if val =='*':
    injured_idx = idx
    continue
  if idx % 2:
    sum += int(val) * 3
  else:
    sum += int(val)


if injured_idx % 2:
  for i in range(10):
    if (sum + i * 3) % 10 == 0:
      print(i)
      break
else:
  print(10 - sum % 10)
