# boj 1138

from sys import stdin

n = int(stdin.readline())

li = list(map(int, stdin.readline().split()))

def solution(n, li):
    result = [0] * n

    for i in range(n):
        cnt_zero = 0

        for j in range(n):
            if cnt_zero == li[i] and result[j] == 0:
                result[j] = i + 1  # 수 1 ~ N
                break
            elif(result[j] == 0):
                cnt_zero += 1

    return result

print(*solution(n, li))