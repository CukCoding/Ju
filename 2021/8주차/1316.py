#그룹 단어란 단어에 존재하는 모든 문자에 대해서, 
# 각 문자가 연속해서 나타나는 경우만을 말한다. 
# 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, 
# kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, 
# aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

def check(arr): #반복되지않은 문자열로 바꾸는 함수
    check_arr = ""
    if(len(arr)):
        check_arr = arr[0] #arr배열의 첫번째 문자를 check_arr에 집어넣는다
    for i in range(1,len(arr)): #arr배열의 두번째 문자부터 check_arr와 문자가 같은지 비교한다.
        if check_arr[-1] != arr[i]: # 문자가 같지않다면 반복되지않는것이므로 check_arr 배열에 arr[i]의 문자를 집어넣는다.
            check_arr += arr[i]
            
    #print("문자열",check_arr)

    for i in range(len(check_arr)): # check_arr 배열안에 중복문자가 있는지 검사한다.
        for j in range(len(check_arr)):
            if j != i:
                if(check_arr[i] == check_arr[j]): # 반복되지않는 문자열속에서 중복 문자가 나온다면 그것은 그룹단어가 아니다.
                    return 0
    return 1

N = int(input())
count = 0 

for i in range(N):
    count += check(input())
    #print(count)

print(count)







