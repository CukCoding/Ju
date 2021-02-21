#둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로 주어진다. 

#스택에 1부터 입력받은 값까지 차례대로 push한다.
#입력받은 값과 같아지면 pop한다. 
#입력받은 값과 같지않으면 수열을만들수없다.

N = int(input())
result_stack = []
stack = []
count = 0 
result = 1

for i in range(N):
    num = int(input()) 

    while count < num: #수열을 입력받는 즉시 stack에 num까지의 값을 append한다.
        count += 1 #count가 num보다 커지면 탈출한다.
        stack.append(count)
        result_stack.append("+") 

    if stack[-1] == num: #stack의 마지막 값과 num의 값이 같다면 pop해서 꺼낸다.
        stack.pop()
        result_stack.append("-")
    
    elif stack[-1] != num: #stack의 마지막 값과 num의 값이 같지않다면 더이상 진행이 되지않으므로 NO가 된다.
        result = 0

if result == 0:
    print("NO")
else:
    print("\n".join(result_stack))

    
    
