import sys

input = sys.stdin.readline

count = 0
def recursion(str, left, right) -> int :
    global count
    count +=1 
    if (left >= right) : return 1 
    elif(str[left] != str[right]) : return 0 
    else : return recursion(str, left+1, right-1) 

def is_palindrome(str) :
    return recursion(str, 0, len(str) - 1) 

for _ in range(int(input())) :
    count = 0
    temp = input().strip()
    print(is_palindrome(temp), count)