#첫째 줄에 상근이가 받은 메시지가 주어진다. 이 메시지는 알파벳 소문자로만 이루어져 있고, 최대 100글자이다.

N = input()
cnt = 0
tmp = 0
R=1
C=len(N)

for i in range(1,len(N)): 
    if len(N) % i ==0: # R값이 가장큰 행렬을 구하기 위함
        avg = len(N) / i # 1 * 16, 2 * 8 처럼 좌변값이 우변값을 나누는 형태임
        if i >=avg: #R값이 가장큰경우
            if i > avg: # R이 C보다 클경우 스왑
                R = int(avg)
                C = i
                break
            R = i #열
            C = int(avg) #행
            break
    

arr = [ [0] * C for _ in range(R)] # 2차원 배열 초기화
print(R,C,arr)

for i in range(C): 
    for j in range(R): # 
        arr[j][i] = N[cnt] #세로로 값 입력하기 (암호화)
        cnt += 1 

for i in range(R):
    for j in range(C):
        print(arr[i][j],end='') #가로로 출력하기

