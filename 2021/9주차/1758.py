#각 손님은 강호에게 
# 원래 주려고 생각했던 돈 - (받은 등수 - 1) 음수면 안준다.
#민호(3원), 재필(2원), 주현(1원)이 순서대로 줄을 서있다면, 
#민호는 강호에게 3-(1-1) = 3원, 재필이는 2-(2-1) = 1원, 주현이는 1-(3-1) = -1원을 
# 팁으로 주게 된다. 주현이는 음수이기 때문에, 강호에게 팁을 주지 않는다. 
# 따라서, 강호는 팁을 3+1+0=4원을 받게 된다.

N = int(input())
arr = [0]*N
money = 0
for i in range(N):
    arr.append(int(input()))

arr.sort(reverse=True)

i=0

while True:
    if arr[i] -((i+1)-1) >= 0:
        money += arr[i] - ((i+1)-1)
    else:
        break
    i += 1

print(money)