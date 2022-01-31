def SetACM():
    cnt = 0
    breaker = False
    for i in range(0,W):
        for j in range(0,H):
            cnt += 1
            if cnt == N:
                breaker = True
                hosu = (j+1)*100 + (i+1)
                return hosu
        if breaker == True:
            break

T = int(input())
result = [] 
for i in range(T):
    H,W,N = map(int,input().split())
    result.append(SetACM()) 

for i in range(T):
    print(result[i])
