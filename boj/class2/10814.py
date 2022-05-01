# https://www.acmicpc.net/problem/10814

from sys import stdin

n = int(stdin.readline())

ageList = [[] for _ in range(201)]

for _ in range(n):
  [age, name] = stdin.readline().split()

  ageList[int(age)].append(name)

for age in range(1, 201):
  if ageList[age]:
    for name in ageList[age]:
      print(f"{age} {name}")