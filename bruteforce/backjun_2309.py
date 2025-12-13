import sys
import itertools

input = sys.stdin.readline

arr = []
for _ in range(9) : 
    arr.append(int(input()))

nCr = itertools.combinations(arr,7)
answer_arr = []
for comb in nCr : 
    if(sum(comb) == 100) :
        answer_arr = comb 
        break 

s_arr = sorted(list(answer_arr))
for s in s_arr : 
    print(s)