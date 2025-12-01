import sys 
import math 

input = sys.stdin.readline 

n,k = map(int,input().split())

is_prime = [True] * (n+1)

count = 0 
answer = 0
for i in range(2,n+1) :
    if(is_prime[i]) :

        for j in range(i,n+1,i) :
            if(is_prime[j]) :
                # print(j)
                is_prime[j]= False
                count += 1
                if(count == k) :
                    answer= j 
                    break 
    if(answer != 0) :
        break 
print(answer)



