from sys import stdin
input = stdin.readline

N, M = map(int, input().rstrip().split())

passwords = {}

for _ in range(N):
  site, password = input().rstrip().split()
  passwords[site] = password

sites = []
for _ in range(M):
  sites.append(input().rstrip())

for site in sites:
  print(passwords[site])