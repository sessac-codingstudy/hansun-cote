import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split()))

idx = n - 1
check = False
for i in range(n-1, 0, -1) :
    f = arr[i-1]
    b = arr[i] 
    if(f > b) :
        arr[i-1], arr[i] = arr[i], arr[i-1]
        check = True 
        break 

if(check) :
    print(' '.join(str(a) for a in arr))
else : 
    print(-1) 

