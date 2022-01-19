#가장 짧은, 가장 빠른이면 bfs로해라
import sys 
from collections import deque 

input = sys.stdin.readline() 

def bfs(): 
    q = deque() 
    q.append(N) 
    while q:
        x = q.popleft() #시작점 5 10 9 18 17순이면 4초면찾는다
        if x == K: # 동생이있는 위치일때 종료
            print(dist[x]) 
            break 
        for j in (x-1,x+1,x*2): #1초뒤에 갈수있는 경우의수
            if 0<= j <= MAX and not dist[j]: #dist는 0배열이라 not dist로 해서 값들어갈때까지돌림
                dist[j] = dist[x] +1 #방문표시겸 시간초 카운트
                q.append(j) #큐에 경우의수 넣어줌

MAX = 100000 
N,K = map(int,input.split()) 
dist = [0] * (MAX+1) #이동하는거리 알기위함
bfs()
