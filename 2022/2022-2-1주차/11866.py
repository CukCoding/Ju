from collections import deque

N,K = map(int,input().split())

lst = [i for i in range(1,N+1)]
queue = deque(lst)
num = 0
result = []

for i in range(N):
    for j in range(K-1):
        queue.append(queue.popleft())
    result.append(queue.popleft())

cnt = 1
print('<', end="")
for i in result:
    print(i,end="")
    if cnt != len(result):
        print(', ',end="")
    cnt +=1 
print('>')