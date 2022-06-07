# https://www.acmicpc.net/problem/7568

from sys import stdin

N = int(stdin.readline())

persons = []

for _ in range(N):
    x, y = map(int, stdin.readline().split(" "))
    persons.append([x, y])

orders = []

for a in persons:
    cnt = 1
    for b in persons:
        if a[0] < b[0] and a[1] < b[1]:
            cnt += 1
    orders.append(cnt)

for order in orders:
    print(order, end=" ")
