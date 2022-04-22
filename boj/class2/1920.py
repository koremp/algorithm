# https://www.acmicpc.net/problem/1920

from sys import stdin

n = int(stdin.readline())
arrN = sorted(list(map(int, (stdin.readline().split(' ')))))

m = int(stdin.readline())
arrM = list(map(int, (stdin.readline().split(' '))))

def solution(x):
  start = 0
  end = n - 1

  while start <= end:
    mid = (start + end) // 2
    if x == arrN[mid]:
      return 1
    elif x < arrN[mid]:
      end = mid - 1
    elif x > arrN[mid]:
      start = mid + 1
  
  return 0

for item in arrM:
  print(solution(item))