#유클리드 호제법
def gcd(x,y):
    mod = x % y
    while mod >0:
        x = y
        y = mod
        mod = x % y
    return y

#입력함수
N = int(input())
freight = [] # 입력값
for _ in range(N):
    freight.append(int(input()))

freight.sort(reverse = True)
num_min = min(freight) #최솟값 찾기
freight.remove(num_min) #최솟값 제거

for i in range(len(freight)):
    if(freight[i] > num_min):
        freight[i] = freight[i] - num_min #모든 정수에 최솟값을 뺴준다.

gcd_arr= freight[0] #gcd함수에서 최대공약수를 찾기위해 배열첫번째값을 gcd_arr에 저장한다.
for i in range(len(freight)):
    gcd_arr = gcd(gcd_arr,freight[i])

for i in range(2,gcd_arr+1):
    if(gcd_arr%i == 0):
         print(i, end=' ')




    
