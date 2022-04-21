# https://www.acmicpc.net/board/view/80076

from sys import stdin
from collections import deque

def sol():
    n = int(stdin.readline())
    nums = deque(range(1, n+1)) #1~n까지 들어있는 리스트
    stack = [0]
    cals = []
    
    for _ in range(n):
        a = int(stdin.readline())
        b = len(nums)
        if a == stack[len(stack)-1]: #스택 마지막 원소와 같은지?
            stack.pop()    #pop
            cals.append('-') 
        else:
            for _ in range(b): 
                if nums[0] <= a:    # 스택에 수 추가
                    stack.append(nums[0])
                    nums.popleft()
                    cals.append('+') #push
                else: break
            if a != stack[len(stack)-1]: #push한게 없었다는 뜻. "NO" 출력
                print('NO')
                exit()
            else:
                stack.pop()    #pop
                cals.append('-')
    print('\n'.join(cals))
sol()