#x보다 가까우면 x보다 숙박비가 더 비싸다
#x보다 숙박비가 싸면 x보다 멀다

N = int(input())

arr =[[0] * 2 for _ in range(N) ]

# for i in range(N):
#     for j in range(2):
#         arr[i][j] = list(map(int,input().split()))
for i in range(N):
    arr[i] = list(map(int,input().split()))

print(arr)

count = 0

for i in range(N):
    flag = 1
    for j in range(N):
        if j != i:
            if arr[i][0] > arr[j][0]: #x보다 가까울때
                if arr[i][1] < arr[j][1]: #x보다 숙박비가 더 쌀때
                    flag = 0
                    break
            if arr[i][1] > arr[j][1]: #x보다 숙박비가 더 쌀때
                if arr[i][0] > arr[j][0]: #x보다 거리가 가까울때
                    flag = 0
                    break
    if flag == 1:
        count += 1

print(count) 
                    