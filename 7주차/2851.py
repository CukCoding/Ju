#총 10개의 줄에 각각의 버섯의 점수가 주어진다. 
# 이 값은 100보다 작거나 같은 양의 정수이다. 버섯이 나온 순서대로 점수가 주어진다.

#첫째 줄에 마리오가 받는 점수를 출력한다. 
# 만약 100에 가까운 수가 2개라면 (예: 98, 102) 마리오는 큰 값을 선택한다.

arr = [0] * 10
sum = [0] * 10

for i in range(10):
    arr[i] = int(input())

for i in range(10):
    sum[i] = sum[i-1] + arr[i]
    if sum[i] >= 100:
        if sum[i] - 100 > 100 - sum[i-1]:
            print(sum[i-1])
            if sum[i] - 100 == 100 - sum[i-1]:
                print(sum[i])
        else:
            print(sum[i])
        break