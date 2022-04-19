import sys

[k, n] = map(int, sys.stdin.readline().split())

arr = [int(sys.stdin.readline()) for i in range(k)]

start = 1
end = max(arr)

result = 0
while (start <= end):
    count = 0
    mid = (start + end) // 2
    
    for item in arr:
        count += item // mid
    
    if count < n:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

 print(result)
