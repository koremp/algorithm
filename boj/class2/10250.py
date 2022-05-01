# https://www.acmicpc.net/problem/10250

from sys import stdin

t = int(stdin.readline())

for _ in range(t):
  [height, width, num] = list(map(int, stdin.readline().split(' ')))
  y = num % height    
  x = num // height
  
  if y == 0:
    y = height
  else:
    x += 1
    
  print("{}{:02d}".format(y, x))