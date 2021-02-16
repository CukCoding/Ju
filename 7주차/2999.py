#첫째 줄에 상근이가 받은 메시지가 주어진다. 이 메시지는 알파벳 소문자로만 이루어져 있고, 최대 100글자이다.

N = input()
cnt = 0
R=len(N)
C=1

for i in range(1,len(N)): 
    if len(N) <= 3: #4보다 작으면 2차원배열이 만들어지지 않음
        R=1
        C=len(N)
    elif len(N) % i ==0: # R값이 가장큰 행렬을 구하기 위함
        avg = len(N) / i # 1 * 16, 2 * 8 처럼 좌변값이 우변값을 나누는 형태임
        if avg * i == len(N):
            if i>=avg: #R값이 가장큰경우
                R = i #열
                C = int(avg) #행
                break

arr = [ [0] * C for _ in range(R)] # 2차원 배열 초기화
print(arr)

for i in range(R): 
    for j in range(C): # 10같은 경우에는 5*2배열이다. ㄴㄴ R<=C 위배되니 2*5가 맞음
        arr[j][i] = N[cnt] #세로로 값 입력하기 (암호화)
        cnt += 1 

for i in range(R):
    for j in range(C):
        print(arr[i][j],end='') #가로로 출력하기

