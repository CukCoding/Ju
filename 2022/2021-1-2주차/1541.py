strInput = input()
isMinus = False
num = 0
sum = 0
while(True):
    i = 0
    if strInput[i] != '-' and isMinus == False:
        num += strInput[i]
    if strInput[i] == '-' and isMinus == True:
        isMinus = False
        num-=sum
        sum = 0
    if strInput[i] == '-':
        sum += strInput[i]

