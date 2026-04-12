from sys import stdin

str = stdin.readline().rstrip()
isPalindrome = True

if len(str) == 1:
  print('true')
else:
  for x in range(len(str) // 2):
    if str[x] != str[len(str) - x - 1]:
      isPalindrome = False
      break

  print('true' if isPalindrome else 'false')