import sys
import math 
input = sys.stdin.readline

tc = int(input())

def check(n) : 
    arr = [False] * (n+1) 
    for i in range(1,n+1) :
        # print("here", i)
        
        for j in range(i,n+1,i) :
            arr[j] = not arr[j]
        # print(arr)
    count = 0
    for i in range(1,n+1) :
        if(arr[i]) : count +=1 
    return count



for _ in range(tc) : 
    n = int(input())
    ans = check(n)
    print(ans)
    