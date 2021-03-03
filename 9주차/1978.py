def sosu(x):
    if x == 1:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
    return True 

N = int(input())
count = 0
check = 0

arr = []
arr = list(map(int,input().split()))

for i in range(N):
    check = sosu(arr[i])
    if check == True:
        count += 1

print(count)
