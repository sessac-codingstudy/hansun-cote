import sys 

input = sys.stdin.readline 
arr = [] 
for _ in range(10) : 
    arr.append(int(input()))

for i in range(9) : 
    arr[i+1] = arr[i] + arr[i+1]

min_v = sys.maxsize
answer = 0
for item in arr : 
    if(abs(100-item) <= min_v) :
        answer = item 
        min_v = abs(100-item)
    

print(answer)
