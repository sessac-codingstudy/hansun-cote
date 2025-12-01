import sys
input = sys.stdin.readline

n = int(input())
lst = [] 
for _ in range(n) : 
    lst.append(int(input()))

lst.sort()
res = 0
for i in range(n) : 
    res = max(lst[i] * (n-i),res)
print(res)