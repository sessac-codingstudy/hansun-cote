import sys
input = sys.stdin.readline

n = int(input())
fruit_dict = {} 
for _ in range(n) : 
    word,count = input().split()
    if word in fruit_dict :
        fruit_dict[word] += int(count) 
    else :
        fruit_dict[word] = int(count) 
    
answer = "NO"
for k,v in fruit_dict.items() : 
    if(v == 5) :
        answer = "YES"
print(answer)
    