N = int(input())
size_list = list(map(int, input().split()))
T, P = map(int, input().split())
count = 0

for i in size_list:
  if i > 0:
    if i % T != 0:
      count += i // T + 1
    else:
      count += i // T

print(count)
print (N // P, N % P)