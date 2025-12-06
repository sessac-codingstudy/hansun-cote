import sys
input = sys.stdin.readline

tc = int(input())

for _ in range(tc) :
    n = int(input())
    cloths_dict = {} 
    for _ in range(n) :
        cloth, kinds = input().split()
        if kinds in cloths_dict :
            cloths_dict[kinds].append(cloth)
        else : 
            cloths_dict[kinds] = [cloth]
    
    temp = 1
    for k,v in cloths_dict.items() : 
        temp *= len(v)+1 
    print(temp - 1)
