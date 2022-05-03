# https://www.acmicpc.net/problem/10828

from sys import stdin


class STACK:
    def __init__(self):
        self.values = []
        self.size = 0

    def push(self, value):
        self.values.append(value)
        self.size += 1

    def pop(self):
        if self.empty():
            return -1
        else:
            self.size -= 1
            return self.values.pop()

    def empty(self):
        if self.size == 0:
            return 1
        else:
            return 0


n = int(stdin.readline().rstrip())
stack = STACK()

for i in range(n):
    order = list(stdin.readline().split())
    if order[0] == "push":
        stack.push(int(order[1]))
    elif order[0] == "pop":
        print(stack.pop())
    elif order[0] == "size":
        print(stack.size)
    elif order[0] == "empty":
        print(stack.empty())
    else:
        if stack.empty():
            print(-1)
        else:
            print(stack.values[-1])
