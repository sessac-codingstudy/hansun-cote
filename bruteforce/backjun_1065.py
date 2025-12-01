import sys
input = sys.stdin.readline

n = int(input())
count = 0 
def func(num):
    
    global count
    if(num < 10) :
        count += 1
        return  
    lst = [] 
    while(num >= 10) :
        lst.append(num%10)
        num //= 10 
    lst.append(num)
    diff = lst[-1] - lst[-2]
    for i in range(0,len(lst) - 1) :
        if(lst[i+1] - lst[i]) != diff :
            return 
    count += 1

for i in range(1,n+1) : 
    func(i) 
print(count)