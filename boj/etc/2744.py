from sys import stdin

word = stdin.readline().rstrip()

reversed_word = []

ord_small_a = ord('a')
ord_large_a = ord('A')
ord_small_z = ord('z')
ord_large_z = ord('Z')

for c in word:
  ord_c = ord(c)

  if ord_small_a <= ord_c and ord_small_z >= ord_c:
    print(c.upper(), end='')
  else:
    print(c.lower(), end='')

