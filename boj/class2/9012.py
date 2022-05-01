# https://www.acmicpc.net/problem/9012

from sys import stdin

n = int(stdin.readline())
parenthesis, answer = [], []

for _ in range(n):
  parenthesis.append(stdin.readline().strip())

def parenthesis_checker(line):
  stack = [line[0]]
  for letter in line[1:]:
    if stack:
      if letter == ")" and stack[-1] == "(":
        stack.pop()
      else:
        stack.append(letter) 
    else:
      stack.append(letter)
  if stack:
    return "NO"
  return "YES"


for line in parenthesis:
  if line[0] == ")" or line[-1] == "(":
    answer.append("NO")        
  else:    
    result = parenthesis_checker(line)
    answer.append(result)

for res in answer:
  print(res)