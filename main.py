import sys

input = sys.stdin.readline

def check_palindrom(word) : 
    length = len(word)
    for i in range(length//2+1) :
        if(word[i] != word[length-i]) :
            return False 
    
    return True 

while(True) : 
    word = input()
    
    if(word == '0') :
        break 

    print(check_palindrom(word))
