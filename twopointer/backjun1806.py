#백준 1806 

import sys 
input = sys.stdin.readline
N,S = map(int,input().split())
arr= list(map(int,input().split()))

l_pointer = 0 
r_pointer = 0
sum = arr[0]
min_length = sys.maxsize

while(l_pointer <= r_pointer and r_pointer < len(arr)) : 
    
    if(sum >= S) : 
        arr_length = r_pointer - l_pointer + 1 
        min_length = min(min_length, arr_length)
        sum = sum - arr[l_pointer]
        l_pointer += 1 

    elif(sum < S) :
        if(r_pointer+1 >= len(arr)) :
            break 
        sum = sum + arr[r_pointer+1]
        r_pointer += 1 

if(min_length == sys.maxsize) :
    print(0)
else :
    print(min_length)
        
    
