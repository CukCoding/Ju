# A를 내림차순 정렬후 B원소와 더한값에서 가장 작은값을 sum에 곱해서 넣음
# 그 값을 배열에서 없애고 다시 for문 반복
N = int(input())
A = []
B = []

for i in range(N):
    A.append(int(input()))
for i in range(N):
    B.append(int(input()))

A.sort(reverse=True)
temp = 0
sum = 0
print(A)
flag = 0
for i in range(0,N):
    for j in range(0,B.__len__()):
        print(j)
        if temp > A[i] + B[j]: 
            temp = A[i] + B[j]
            flag = j
            print(flag,'dasdsa')
            print(temp)
    print(B)
    sum += A[i] * B[j]
    B.pop(flag)
    

print(sum)