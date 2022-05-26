# https://www.acmicpc.net/problem/2869

from sys import stdin

a, b, v = map(int, stdin.readline().split(" "))

if a == v:
    print(1)
else:
    x = (v - b) // (a - b)

    if (v - b) / (a - b) > x:
        x += 1
    
    print(x)
