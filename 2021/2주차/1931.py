n = int(input())
room = []

for i in range(n):
    start, end= map(int, input().split())
    room.append([start, end]) #key:value 형식으로 입력 1,4 2,3 이런식으로 받기위함

room.sort(key = lambda x:(x[1],x[0])) #끝나는 시간으로 우선정렬 후 같으면 시작시간으로 정렬

cnt = 1
end_time = room[0][1] # 가장 첫번째 회의 종료시간

for i in range(1,n):
    if room[i][0] >= end_time: # 첫번째 회의 종료 시간보다 큰 시작 시간을 가져옴
        cnt += 1
        end_time = room[i][1] # 종료 시간에 해당 시작 시간을 집어넣음

print(cnt)