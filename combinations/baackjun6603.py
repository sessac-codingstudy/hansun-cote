import sys
input = sys.stdin.readline

from itertools import combinations
while(True) : 
    arr = list(map(int,input().split()))
    if(arr[0] == 0 ) :
        break 
    items = arr[1:]
    answer_list = list(combinations(items,6))
    for ans in answer_list :
        for i in ans :
            print(i,end=' ')
        print()
    print()
    
            

