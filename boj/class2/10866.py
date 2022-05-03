# https://www.acmicpc.net/problem/10866

from sys import stdin
from collections import deque


class Deque:
    def __init__(self):
        self.items = deque()

    def push_front(self, X):
        self.items.appendleft(X)

    def push_back(self, X):
        self.items.append(X)

    def empty(self):
        return int(not self.items)

    def pop_front(self):
        if self.empty():
            return -1
        return self.items.popleft()

    def pop_back(self):
        if self.empty():
            return -1
        return self.items.pop()

    def size(self):
        return len(self.items)

    def front(self):
        if self.empty():
            return -1
        return self.items[0]

    def back(self):
        if self.empty():
            return -1
        return self.items[-1]


dq = Deque()
num = int(stdin.readline())

for _ in range(num):
    string = stdin.readline().rstrip()
    if string == "size":
        print(dq.size())
    elif string == "empty":
        print(dq.empty())
    elif string == "pop_front":
        print(dq.pop_front())
    elif string == "pop_back":
        print(dq.pop_back())
    elif string == "front":
        print(dq.front())
    elif string == "back":
        print(dq.back())
    else:
        temp, n = string.split()
        n = int(n)
        if temp == "push_front":
            dq.push_front(n)
        else:
            dq.push_back(n)
