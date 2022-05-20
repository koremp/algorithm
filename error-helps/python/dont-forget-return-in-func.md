# 함수에서 return 까먹지 말기

왜냐면 계속 함수에서 안쓰고 main에서 while문 돌리고 그래서 까먹었음

```python
# https://www.acmicpc.net/problem/2805

from sys import stdin


def findMax(heights):
    start = 0
    last = max(heights)

    while start <= last:
        middle = (start + last) // 2
        sum = 0

        for height in heights:
            if height >= middle:
                sum += height - middle

        if sum >= m:
            start = middle + 1
        else:
            last = middle - 1

    return last


n, m = map(int, stdin.readline().split(" "))
heights = list(map(int, stdin.readline().split(" ")))

print(findMax(heights))
```