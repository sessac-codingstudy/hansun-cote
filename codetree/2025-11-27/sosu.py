a, b = map(int, input().split())

# Please write your code here.
def is_prime(n) :

    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False

    if is_prime:
        return True
    else:
        return False 


sum_v = 0 
for i in range(a, b+1) :
    if(is_prime(i)) :
        sum_v += i 

print(sum_v)