#첫째 줄부터 다섯째 줄까지 빙고판에 쓰여진 수가 
# 가장 위 가로줄부터 차례대로 한 줄에 다섯 개씩 빈 칸을 사이에 두고 주어진다. 
# 여섯째 줄부터 열째 줄까지 사회자가 부르는 수가 차례대로 한 줄에 다섯 개씩 빈 칸을 사이에 두고 주어진다. 
# 빙고판에 쓰여진 수와 사회자가 부르는 수는 각각 1부터 25까지의 수가 한 번씩 사용된다.

N=5
count = 0
V = [0] * N #가로 체크
H = [0] * N # 세로 체크
cross = 0 #대각선 체크
cross2 = 0 #역대각선 체크

def check(host):
    for i in range(N):
        for j in range(N):
            if bingo[i][j] == host: #해당 좌표 값과 사회자 부른값 비교
                V[i] += 1 
                H[j] += 1
                if i == j: #대각선일때
                    cross += 1
                if i+j == N-1: #역대각선일때
                    cross2 += 1
            if V[j] == N-1: #가로 빙고
                count += 1
            elif H[j] == N-1: #세로 빙고
                count += 1 
            elif cross == N-1: #대각선 빙고
                count +=1
            elif cross2 == N-1: #역대각선 빙고
                count +=1


bingo = [list(map(int, input().split()))for _ in range(N)] # 5*5를 만듦
host = []

for i in range(N):
    host += list(map(int, input().split()))

ans = 0
for i in host:
    print("사회자값",i)
    ans += 1
    if check(i) == True:
        break

