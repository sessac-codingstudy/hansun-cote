백준 1002 
import math 

n = int(input())

for _ in range(n) :
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    temp = r1+r2 
    
    #같은 좌표를가질때
    if(distance == 0) :
        #반지름이 똑같을경우
        if(r1 == r2) :
            print(-1)
        #반지름이 다를경우 
        else :
            print(0)
    # 내접
    elif(distance == abs(r1-r2)) :
        print(1)
    # 내부에서 만나지 않을 경우 
    elif(distance  < abs(r1-r2)) :
        print(0)
    # 외접
    elif(distance == temp) :
        print(1)
    # 두 접에서 만남 
    elif(distance < temp) :
        print(2) 
    # 만나지 않음 
    elif(distance > temp ) :
        print(0)
    else :
        print(1)
        

    

s
