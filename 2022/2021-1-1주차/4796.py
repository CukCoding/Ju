#L 일동안만 사용가능
#캠핑일 P
#휴가 일수 V
# 20 / 8 = 2 * 5  10 + (20 % 8) = 14 
#최소 일수(V/P)*L를 구하고 남은 일수를 더한다.

count = 1
while True:
    #L = 휴가일, P = 캠핑일 , L = 사용가능일
    L, P, V = map(int, input().split())
    if L == P == V == 0: 
        break # 0 0 0입력시 종료
 
    result = V//P * L 
    result += min(V % P, L) # V%P 가 L보다 크면안됨 만약 크다면 V를 더해주어야함. 
    print(f'Case {count}: {result}')
    count += 1

