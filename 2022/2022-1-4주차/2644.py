from collections import deque

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = True
    ans = 0
    while q:
        ans += 1 #촌수 관계가있다면 1 증가
        for _ in range(len(q)): #큐의 개수만큼 큐에서 값뺀다.
            k = q.popleft()
            if k == b:
                return ans-1
            for e in arr[k]: #입력받았던 배열의 값 만큼 돌린다
                if visited[e] == False: #방문하지않았을때
                    visited[e] = True
                    q.append(e) #큐에 담는다.

    return -1 # 촌수관계없을시 -1출력
n = int(input())
a, b = map(int ,input().split(' '))
m = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(m): #촌수 배열에 저장
    x, y = map(int, input().split(' '))
    arr[x].append(y)
    arr[y].append(x)

visited = [0] * (n+1) #배열 초기화
print(bfs(a))