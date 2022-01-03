L = int(input()) #L일동안만 사용가능
P = int(input()) #P일
V = int(input()) #휴가

sub = P-L
vArr = []
for i in range(0,V):
    vArr.append(i+1)

count = 0
cnt = 0
for i in range(0,V):
    cnt +=1
    count += 1
    if count == L:
        if cnt == V:
            break
        for i in range(0,sub):
            vArr.pop()
            print(vArr)
        count = 0
    
print(vArr)
        