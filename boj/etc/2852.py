# boj 2852

from sys import stdin

n = int(stdin.readline())

lines = []

for i in range(n):
    lines.append(stdin.readline())

def solution(n, lines):
    flag = 0
    a_time = 0
    b_time = 0
    previous_time = 0

    for line in lines:
        [team, time] = line.split(' ')
        [min, sec] = list(map(int, time.split(':')))
        cur_time = (min * 60) + sec - previous_time

        print(team, min, sec, cur_time, flag)

        if flag > 0:
            a_time += cur_time
        elif flag < 0:
            b_time += cur_time

        previous_time += cur_time

        if team == '1':
            flag += 1
        elif team == '2':
            flag -= 1

    if flag > 0:
        a_time += 2880 - previous_time
    elif flag < 0:
        b_time += 2880 - previous_time

    print(f'{a_time // 60:02}:{a_time % 60:02}')
    print(f'{b_time // 60:02}:{b_time % 60:02}')

solution(n, lines)
