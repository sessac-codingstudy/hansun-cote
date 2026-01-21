import sys 
input = sys.stdin.readline 

n = int(input().strip())

arr = [] 
for _ in range(n) : 
    arr.append(int(input().strip()))

for t in sorted(arr) :
    print(t)