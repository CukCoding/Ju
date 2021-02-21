#총 10개의 줄에 각각의 버섯의 점수가 주어진다. 
# 이 값은 100보다 작거나 같은 양의 정수이다. 버섯이 나온 순서대로 점수가 주어진다.

#첫째 줄에 마리오가 받는 점수를 출력한다. 
# 만약 100에 가까운 수가 2개라면 (예: 98, 102) 마리오는 큰 값을 선택한다.

arr = [0] * 10
sum = [0] * 10

for i in range(10):
    arr[i] = int(input())

for i in range(10):
    sum[i] = sum[i-1] + arr[i] #sum배열에 값을 누적시킨다.
    if sum[i] >= 100: #누적된값이 100보다 커질때
        if sum[i] - 100 == 100 - sum[i-1]: #차이가 똑같을경우
            print(sum[i]) #더 큰값을 출력
            break
        elif sum[i] - 100 > 100 - sum[i-1]: # 현재값에서 100을 뺸 값과 100에서 과거값의 차이를 비교한다. 
            print(sum[i-1]) # 현재값에서 100을 뺸값이 더 크다는것은 과거값이 100에 더 근접하다는 의미이다.
            break
        else:
            print(sum[i])
            break
    if i == 9 and sum[i] < 100:
        print(sum[i])

# for i in range(10):
#     sum[i] = sum[i-1] + arr[i] #sum배열에 값을 누적시킨다.
#     if sum[i] >= 100: #누적된값이 100보다 커질때
#         if sum[i] - 100 > 100 - sum[i-1]: # 현재값에서 100을 뺸 값과 100에서 과거값의 차이를 비교한다. 
#             print(sum[i-1]) # 현재값에서 100을 뺸값이 더 크다는것은 과거값이 100에 더 근접하다는 의미이다.
#             if sum[i] - 100 == 100 - sum[i-1]: # 
#                 print(sum[i])
#         else:
#             print(sum[i])
#         break