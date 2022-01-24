strInput = input().split('-')
sum = 0
for i in strInput[0].split('+'): # 첫번쨰- 가 나오기전까지의 수를 모두 더한것
    sum += int(i)

for i in strInput[1:]: #그 뒤로부터 다 빼주는데 +가 묶인애들도 있으므로 분리하기위해 +로 split 위에서 -기준으로 split했기에 +로묶였을거임
    for j in i.split('+'):
        sum -= int(j)

print(sum)

