#첫째 줄에 상근이가 받은 메시지가 주어진다. 이 메시지는 알파벳 소문자로만 이루어져 있고, 최대 100글자이다.

N = input()

cnt = 0
for i in range(1,len(N)):
    if len(N) % i ==0: # R값이 가장큰 행렬을 구하기 위함
        avg = len(N) / i # 1 * 16, 2 * 8 처럼 좌변값이 우변값을 나누는 형태임
        if avg<=i: #R값이 가장큰경우
            R = int(avg) #열
            C = i #행
            break

arr = [ [0] * R for _ in range(C)] # 2차원 배열 초기화


for i in range(R):
    for j in range(C):
        arr[j][i] = N[cnt] #세로로 값 입력하기 (암호화)
        cnt += 1 

for i in range(R):
    for j in range(C):
        print(arr[i][j],end='') #가로로 출력하기

