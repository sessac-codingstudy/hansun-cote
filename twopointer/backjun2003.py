import sys
input = sys.stdin.readline

n, m = map(int,input().split())
arr = list(map(int,input().split()))
left = 0
right = 0
count = 0
s_value = arr[right]
while(left<=right and right < n) :
    if(s_value < m) :
        right +=1 
        if(right == n) :
            break
        s_value += arr[right]
    elif(s_value > m) : 
        s_value -= arr[left]
        left +=1 
    else : 
        count += 1
        right +=1 
        if(right == n) :
            break
        s_value += arr[right]
print(count)

