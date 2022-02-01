from collections import deque

N,K = map(int,input().split())

lst = [i for i in range(1,N+1)]
queue = deque(lst)
num = 0
result = []

for i in range(N):
    for j in range(1,K):
        num = queue.popleft()
        queue.append(num)
    result.append(queue.popleft())

print(result)