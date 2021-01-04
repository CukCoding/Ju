H,M = map(int, input().split())
Arm = 60

if(M<45):
    Arm -= (45-M)
    if(H == 0):
        H = 23
    else:
        H -= 1
    print(H,Arm)

else:
    M -= 45
    print(H,M)
