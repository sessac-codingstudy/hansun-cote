import sys 

n = int(sys.stdin.readline())

stack = [] 
for _ in range(n) : 
    temp = list(input().split())
    if(temp[0] == "push") :
        stack.append(int(temp[1]))
    elif(temp[0] == "pop") :
        if(len(stack) == 0) :
            print(-1)
        else :
            print(stack.pop())
    elif(temp[0] == "size") :
        print(len(stack)) 
    elif(temp[0] == "empty") : 
        if(len(stack) == 0) :
            print(1)
        else :
            print(0)
    else :
        if(len(stack) == 0) :
            print(-1)
        else :
            print(stack[-1])
