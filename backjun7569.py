# 백준 7569

import sys 
from collections import deque
input = sys.stdin.readline

move = [ [1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,-1],[0,0,1]]
#초기화
N, M, H = map(int, input().split())
matrix =[]
copy_matrix = []
que = deque()
visited = [[[False] * N for _ in range (M)] for _ in range(H)]

level = 0 
for h in range(H) :
    plane = []
    for i in range (M):
        temp = list(map(int, input().split()))
        for j in range(N) : 
            if(temp[j] == 1) :
                que.append((i,j,h,level))
                visited[h][i][j] = True
        plane.append(temp)
    matrix.append(plane)
    copy_matrix.append([row[:] for row in plane])  


while que :
    item = que.popleft()

    ## level 갱신 
    level = item[3]

    for m in move : 
        next_x = item[0] + m[0]
        next_y = item[1] + m[1]
        next_z = item[2] + m[2] 
        
        next_level = item[3] + 1
        ##범위를 벗어난 곳이라면
        if(next_x < 0 or next_y < 0 or next_z < 0 or next_x >= M or next_y >= N or next_z >= H) :
            continue 

        ##이미 방문한 곳이라면 
        if(visited[next_z][next_x][next_y]) :
            continue

        ##-1이라면 
        if(matrix[next_z][next_x][next_y] == -1) :
            continue

        visited[next_z][next_x][next_y]= True
        copy_matrix[next_z][next_x][next_y] = 1
        que.append((next_x, next_y, next_z, next_level))

for h in range(H) :
    for i in range(M) : 
        for j in range(N) :
            if(copy_matrix[h][i][j] == 0) :
                print(-1)
                exit() 



print(level)




