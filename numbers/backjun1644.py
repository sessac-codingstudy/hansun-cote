import sys 
import math 

input = sys.stdin.readline 

n = int(input())

def eratos(n):
    is_prime = [True] * (n+1)
    if(n<=1) : 
        return [] 
    for i in range(2,int(math.sqrt(n))+1) :
        if(is_prime[i] == True) :
            for j in range(i*2,n+1,i) : 
                is_prime[j] = False 
    
    p_lst = [] 
    for i in range(2,n+1) :
        if(is_prime[i]) :p_lst.append(i)
    return p_lst

prime_lst = eratos(n)
if(prime_lst != []) :
    
    left = 0
    right = 0
    sum_v = prime_lst[left]
    count = 0 
    length = len(prime_lst)
    # print(prime_lst)
    while(left<=right and right < length and left < length) :
        # print(left, right,sum_v)
        if(sum_v < n) :
            right += 1
            if(right == length) : 
                break

            sum_v += prime_lst[right]
        elif(sum_v > n) : 
            sum_v -= prime_lst[left]
            left += 1 
            if(left == length) :
                break
        else :
            count += 1 
            right +=1
            if(right == length) : 
                break
            sum_v += prime_lst[right]

    print(count)
else :
    print(0)

