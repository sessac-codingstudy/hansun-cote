from collections import deque
import sys 
import copy 
input = sys.stdin.readline 
set_lst = set()

n = int(input())
water_map = []

moving = [[1,0],[0,1],[-1,0],[0,-1]]

def deq_proc(num) : 
    copy_map = copy.deepcopy(water_map)
    visited = [[False] * n for _ in range(n)]
    que = deque()
    count = 0 
    for i in range(n) : 
        for j in range(n) : 
            if(copy_map[i][j] <= num) : 
                visited[i][j] = True 

    for i in range(n) : 
        for j in range(n) : 
            if(not visited[i][j]) :
                count += 1 
                que.append((i,j))
                visited[i][j] = True
                while que : 
                    x,y = que.popleft() 

                    for m in moving : 
                        nx = x + m[0]
                        ny = y + m[1]
                        # print(nx,ny)
                        if( 0 > nx or 0 > ny or n<=nx or n<= ny) :
                            continue
                        if(visited[nx][ny]) :
                            continue
                        que.append((nx,ny))
                        visited[nx][ny] = True 
                        print(visited[nx][ny])    
    # print(visited)
    return count                         

for _ in range(n) : 
    temp = list(map(int,input().split()))
    for c in temp : 
        set_lst.add(c)
    water_map.append(temp)
max_value = 0

for s in set_lst : 
    val = deq_proc(s)   
    print(s, val)
    max_value = max(max_value, val)
print(max_value)