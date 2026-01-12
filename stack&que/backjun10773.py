import sys

input = sys.stdin.readline

count = int(input())
arr = [] 
for i in range(count) :
    num = int(input())
    if(num == 0) :
        arr.pop()
    else :
        arr.append(num) 

print(sum(arr))