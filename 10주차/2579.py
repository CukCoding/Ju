# 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 
# 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 
# 다음 다음 계단으로 오를 수 있다.
# 연속된 세 개의 계단을 모두 밟아서는 안 된다. 
#  단, 시작점은 계단에 포함되지 않는다.
# 마지막 도착 계단은 반드시 밟아야 한다

#초기접근
# i+1번째와 i+2번째를 비교해서 큰 배열에 i를 더해준 뒤 i+1번째가 컸다면 i+1번째부터 for문시작 i+2라면 i+2부터 for문시작 
# 연속된 계단은 두번째까지이다. 연속된계단이 두번째면 그뒤는 비교하지않고 바로 다음 계단으로 간다.
# 처음계단을 무조건 밟아야 이득이다. 따라서 dp[i] = max(dp[i+1],dp[i+2]) 점화식을 세웠다. 
# 시작 계단부터 마지막계단 까지의 경우의수를 했지만 경우의 수가 너무많아서 

# N = int(input())

# dp = [0] * int(N+1)# 7처럼 홀수가 나올경우 7번째 계단을 무조건 밟기 하기위해 N+1만큼 범위를 준다.

# for j in range(N):
#   dp[j] = int(input())

# i=0
# cnt = 0

# while True:
#   if i >= N-1:
#     break

#   if cnt == 2: #연속해서 두번밟을경우 다다음칸으로 넘어감
#     dp[i+2] += dp[i]
#     i += 2
#     cnt = 0
#     continue

#   if dp[i+1] >= dp[i+2]:
#     dp[i+1] += dp[i]
#     i +=1
#     cnt += 1
  
#   elif dp[i+1] <= dp[i+2]:
#     dp[i+2] += dp[i]
#     i += 2

# print(dp[N-1])

#마지막 계단에서부터 시작점까지 계산해보자
# 마지막계단을 무조건 밟는다라면 마지막계단-1일경우 무조건 마지막계단-2를 밟으면 안된다.
# 마지막계단-2라면 뒤에는 뭘 밟든 상관이없다
#dp[i] = max(dp[i-2] + arr[i] , dp[i-3] + arr[i] + arr[i - 1]) 점화식을 세울 수 있다.
# 연속된 계단의 수를 알기위해서 dp[i-1]이아닌 arr[i-1]로 한다. dp로 받아버리면 
# 메모이제이션된 배열을 기억할수가없다. 
# append함수로 배열에 입력을 받을경우 O(1)로 가장빠르다.

import sys
input = sys.stdin.readline

N = int(input())
arr = []
dp = []

for _ in range(N):
  arr.append(int(input()))

dp.append(arr[0])
dp.append(max(arr[0]+arr[1],arr[1]))
dp.append(max(arr[0]+arr[2],arr[1]+arr[2])) # i-3의 인덱스 범위를 설정해주기 위해 0,1,2번째 배열은 값을 미리 입력해준다.

for i in range(3,N): #0,1,2번째는 미리 입력했으므로 3번째배열부터 시작한다.
  dp.append(max(dp[i-2]+arr[i], dp[i-3]+arr[i]+arr[i-1])) 

print(dp[N-1])

