#첫째 줄부터 다섯째 줄까지 빙고판에 쓰여진 수가 
# 가장 위 가로줄부터 차례대로 한 줄에 다섯 개씩 빈 칸을 사이에 두고 주어진다. 
# 여섯째 줄부터 열째 줄까지 사회자가 부르는 수가 차례대로 한 줄에 다섯 개씩 빈 칸을 사이에 두고 주어진다. 
# 빙고판에 쓰여진 수와 사회자가 부르는 수는 각각 1부터 25까지의 수가 한 번씩 사용된다.

#한 라인을 다 더 했을때 0이라면 그것은 1빙고가 된 셈이다.
#저것부터 해서 처음부터 다시 짜야할듯

N=5

def zero(host):
    for i in range(N):
        for j in range(N):
            if bingo[i][j] == host:
                bingo[i][j] = 0
                return 

def check():
    count = 0 
    # 가로빙고
    for i in range(N):
        num_zero = 0
        for j in range(N):
            num_zero += bingo[i][j] #해당 좌표값이 0인지 확인(사회자가 부른값인지)
        if num_zero == 0: #한줄이 싹다 0이면 가로빙고가 완성된것
            count += 1

    # 세로빙고
    for i in range(N):
        num_zero = 0
        for j in range(N):
            num_zero += bingo[j][i] #(0,1),(1,1)...(4,1) 과 같이 j좌표가 다 0이면 세로빙고이다.
        if num_zero == 0: 
            count += 1
    
    #대각선 빙고
    num_zero=0
    for i in range(N):
        num_zero += bingo[i][i] # (0,0),(1,1)과 같이 좌표값이 같은곳이 다 0이면 대각선 빙고이다.
    if num_zero == 0:
        count += 1
    
    #역대각선 빙고
    num_zero=0
    for i in range(N):
        num_zero += bingo[i][N-1-i] # 역대각선을 구하는 공식이다. 이곳이 다 0이면 역대각선 빙고이다.
    if num_zero == 0:
        count += 1
    
    if count >= 3:
        return True
    else:
        return False
    
host = []
bingo = []

bingo = [list(map(int, input().split()))for _ in range(N)] # 5*5를 만듦


for i in range(N):
    host += list(map(int, input().split())) #런타임 오류때문에 입력방식 바꿈

sum = 0

for i in host:
    zero(i)
    sum += 1
    if check() == True: 
        #0부터 시작하기때문에 몇번째인지 아려면 1더해줘야함 아니면 range를 1부터 시작해도될듯
        
        break
        
print(sum)