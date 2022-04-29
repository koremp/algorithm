# https://www.acmicpc.net/problem/4153

from sys import stdin

arr = list(map(int, stdin.readline().split(' ')))
  
while arr != [0, 0, 0]:
  z = max(arr)
  arr.remove(z)

  if z ** 2 == arr[0] ** 2 + arr[1] ** 2:
    print('right')
  else:
    print('wrong')

  arr = list(map(int, stdin.readline().split(' ')))
