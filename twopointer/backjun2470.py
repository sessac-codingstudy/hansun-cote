#백준2470

import sys
input = sys.stdin.readline 
n=int(input())
arr = list(map(int,input().split()))

l = 0 
r = n-1 
min_v = sys.maxsize
best_solution = [0,0]

arr.sort()
while(l<r) :
    now = arr[l] + arr[r]
    if(min_v > abs(now)) :
        min_v = abs(now) 
        best_solution[0] = arr[l]
        best_solution[1] = arr[r]
    
    if(now < 0):
        l += 1 
    elif(now > 0) :
        r -=1
    else :
        print(arr[l], arr[r])
        break 
print(best_solution[0],best_solution[1])

