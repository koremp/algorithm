from sys import stdin

input = lambda: int(stdin.readline().rstrip())

for _ in range(input()):
    d, f, p = map(float, stdin.readline().rstrip().split())
    print('${:.2f}'.format(round(d * f * p, 2)))