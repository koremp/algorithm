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
# print(result) 앞에 빈칸이 하나 있었는데 백준의 코드 작성 환경에서는 에러를 띄워주지 않았다.
# boj 관련 chrome extension이나 vscode extension을 작성하는 방법을 생각해보자
# vscode extension은 애매한 것 같으니 terminal 프로그램으로 제출하는 방법도 괜찮을 것 같다.