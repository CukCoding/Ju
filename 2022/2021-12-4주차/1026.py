# A를 내림차순 정렬후 B원소와 더한값에서 가장 작은값을 sum에 곱해서 넣음
# 그 값을 배열에서 없애고 다시 for문 반복
N = int(input())
A = [int(x) for x in input().strip().split()]
B = [int(x) for x in input().strip().split()]

A.sort(reverse=True)
sum = 0
flag = 0
for i in range(0,N):
    flag = 0
    for j in range(0,N-i):
        if j == 0:
            temp = A[i] * B[j]
        if temp > A[i] * B[j]: 
            temp = A[i] * B[j]
            flag = j
    sum += temp
    B.pop(flag)

print(sum)

    

