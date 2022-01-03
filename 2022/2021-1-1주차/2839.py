# dp배열 선언
# 3원짜리 1개 5원짜리 1개 = dp[3] = 1 , dp[5] = 1 , N이 5보다크면 0으로 채워줌
# 마지막 dp배열의 값이 failNumber랑 같다면 실패한것이므로 -1 출력
# 아니라면 맞게 출력된것이기때문에 해당 값 출력
# 점화식은 dp[i-3]+1 , dp[i-5]+1 둘중 작은값 +1의 의미는 해당 동전을 사용해서 값을구할수있다는 의미(카운트)
N = int(input())
failNumber = 5000
dp = [0,failNumber,failNumber,1,failNumber,1]

if(N>5):
    for i in range(3,N+1):
        dp.append(0)

for i in range(6,N+1):
    dp[i] = min(dp[i - 3] + 1, dp[i - 5] + 1)

if dp[N] >= failNumber:
    print("-1")
else:
    print(dp[N])
