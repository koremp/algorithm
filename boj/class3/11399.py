from sys import stdin
input = stdin.readline

n = int(input().rstrip())
periods = list(map(int, input().rstrip().split()))
periods.sort()

total = 0


for i in range(len(periods)):
  total += sum(periods[:i+1])

print(total)



