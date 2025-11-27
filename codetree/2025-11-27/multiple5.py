n = int(input())

def summing(num) : 
    val = 0
    while num > 10 :
        val += num %10
        num //= 10 
    val += num 
    return val 
# Please write your code here.
if(n%2==0 and summing(n) % 5 == 0) :
    print("Yes")
else :
    print("No")