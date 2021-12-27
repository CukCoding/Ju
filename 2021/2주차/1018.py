n, m = map(int, input().split())
arr = []
result = []

for _ in range(n):
    arr.append(input())

for i in range(n - 7): # 8*8 일때  한번만 돌면되고 그 이상일때 +1번씩 돌면된다.
    for j in range(m - 7):
        wmap = 0
        bmap = 0
        for a in range(i, i + 8): # 위와 마찬가지로 8*8일때 8*8사이즈로 돌리기위해 8을 더해준다.
            for b in range(j, j + 8):              
                if (a + b)%2 == 0: # 홀홀 짝짝 홀짝 짝홀 의 경우 수를 계산하기 위함
                    if arr[a][b] != 'W': wmap += 1  
                    if arr[a][b] != 'B': bmap += 1
                else :
                    if arr[a][b] != 'B': wmap += 1
                    if arr[a][b] != 'W': bmap += 1
        result.append(wmap) 
        result.append(bmap) # 흰색과 검정색 둘다 체크하여 배열에넣고 그중 제일 작은값을 출력한다.                         

print(min(result))   