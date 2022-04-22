# https://www.acmicpc.net/problem/1929
# 에라토스테네스의 체를 이용해 푸는 방법도 있고
# 지금 풀이같이 푸는 방법도 있음.
# 하지만 파이썬 + 지금 풀이는 너무 느리다. stdout.write()를 써주는 것이 좋다.

# 에라토스테네스의 체 참고 : https://www.acmicpc.net/board/view/39203
# 참고 코드 : https://www.acmicpc.net/board/view/80945
# 근데 런타임 에러 2번이나 뜬다.

from sys import stdin

M,N = map(int,stdin.readline().split())

def prime_list(m,n):
  sieve = [True] * (n + 1)
  sieve[0] = False
  sieve[1] = False
  s = int(n ** 0.5)
  
  for i in range(2, s + 1):
    if sieve[i] == True: # i가 소수인 경우
      for j in range(i+i, n+1, i): # i이후 i의 배수들을 False 판정
        sieve[j] = False

  return [i for i in range(m, n + 1) if sieve[i] == True]

for prime in prime_list(M,N):
  print(prime)