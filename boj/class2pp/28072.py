for i in range(3, 0, -1):
    x = input()
    if x not in ['Fizz', 'Buzz', 'FizzBuzz']:
        n = int(x) + i

s = ''
if n % 3 == 0: s += 'Fizz'
if n % 5 == 0: s += 'Buzz'
print(s or n)