#BFS로구현 1컴퓨터와 인접한애들만 더해서 출력해주면됨
from collections import deque

N = int(input()); #컴퓨터 수
graph = [[] for _ in range(N + 1)]

E = int(input()); #연결된 선 수
for _ in range(E): #연결된애들 집어넣기
    i, j = map(int, input().split())
    graph[i][j] = 1
    graph[j][i] = 1

visited = [0] * (N + 1) #0이면 방문안한거

def bfs(graph, start, visited):
    result = 0
    queue = deque([start]) #1번컴퓨터
    visited[start] = 1 #방문했으면 1로바꿈

    while queue: 
        index = queue.popleft() #다음에 방문해야하는곳 팝해서 index에 저장
        for edge in graph[index]: #해당 좌표와 연결된 선만큼
            if not visited[edge]: #연결됐는데 방문을 안헀으면 방문표시하고 감염수 +1
                queue.append(edge)
                visited[edge] = 1
                result += 1
    print(result)

bfs(graph, 1, visited)