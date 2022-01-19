# 힌트: 가장 작은 무게 가방에 무게가 작으면서 비싼 보석을 넣는다.
# 힙은 가장 작은 요소가 항상 heap[0]이다.
import sys
import heapq

N, K = map(int, sys.stdin.readline().split()) #훔칠수있는 보석 , 가방수
boseok = []
for _ in range(N):
    heapq.heappush(boseok, list(map(int, sys.stdin.readline().split()))) # 보석힙에 무게와 가격 입력
bagSize = []
for _ in range(K):
    bagSize.append(int(sys.stdin.readline()))
bagSize.sort() #가방을 오름차순정렬 가장 작은 무게에 가장비싼 보석을 넣기 위함

result = 0
tmp_boseok = [] #가방 무게보다 가벼운 보석담을공간
for bag in bagSize: # 가방 크기만큼 반복
    while boseok and bagSize >= boseok[0][0]: #현재 가방크기보다 작은 보석들만
        heapq.heappush(tmp_boseok, -heapq.heappop(boseok)[1]) #제일 비싼 보석을 넣어준다. 무거운애들은 위에서 이미 걸러냈으므로
    if tmp_boseok:
        result -= heapq.heappop(tmp_boseok) # 최소보다는 작지만 넣을 수 있는 보석이 있을경우
    elif not boseok: #보석 다돌았으면 끝
        break
print(result)