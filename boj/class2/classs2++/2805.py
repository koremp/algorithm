# https://www.acmicpc.net/problem/2805

from sys import stdin

N, M = list(map(int, stdin.readline().split()))
trees = list(map(int, stdin.readline().split()))

# 첫번째 start, end 값
# tallest = max(trees)
# start = tallest - M
# end = tallest - 1

# 두번째 start, end 값
start = 1
end = max(trees)


def getMaxTreeHeight(start, end):
    while start <= end:
        midd = (start + end) // 2
        woods = 0
        for i in trees:
            if i > midd:
                woods += i - midd
        if woods < M:
            end = midd - 1
        else:
            start = midd + 1

        return end


print(getMaxTreeHeight(start, end))
