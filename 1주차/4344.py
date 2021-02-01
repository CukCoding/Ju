n = int(input())

for i in range(n):
    
    arr = list(map(int,input().split()))
    count = 0
    sum1 = sum(arr[1:])
    avg = sum1/arr[0]
    
    for j in arr[1:]:
        if avg < j:
            count += 100

    result = count/arr[0]   
    print("%0.3f%%" % result)
        

