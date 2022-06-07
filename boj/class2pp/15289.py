# https://www.acmicpc.net/problem/11651
# https://www.acmicpc.net/board/view/86925

import string
from sys import stdin


alphabet_list = list(string.ascii_lowercase)
input_length = int(stdin.readline())
input_string = list(stdin.readline().strip())

sum = 0

m = 1234567891
r = 31

for i in range(input_length):
    input_string[i] = alphabet_list.index(input_string[i]) + 1
    sum += input_string[i] * r**i

sum = int(sum % m)
print(sum)
