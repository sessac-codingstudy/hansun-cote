import sys 

input = sys.stdin.readline 
str_arr = list(input().strip())
st_len = len(str_arr) // 10 

for i in range(0, len(str_arr), 10):
    print(''.join(str_arr[i:i+10]))
