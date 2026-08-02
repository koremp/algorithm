import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    numbers_input = input()
    numbers = []

    for i in range(n//4):
        rotated_numbers = numbers_input[len(numbers_input) - i:] + numbers_input[:len(numbers_input) - i]
        for j in range(4):
            numbers.append(rotated_numbers[j * (n//4): (j+1) * (n//4)])

    numbers = list(set(numbers))
    numbers.sort(key=lambda x: int(x, 16), reverse=True)

    result = int(numbers[k-1], 16)

    print(f'{tc} {result}')