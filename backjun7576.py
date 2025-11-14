# 백준 7576 

import sys 
from collections import deque
input = sys.stdin.readline

move = [ [1,0],[-1,0],[0,1],[0,-1]]
#초기화
N, M = map(int, input().split())
matrix =[]
que = deque()
visited = [[False] * N for _ in range (M)]
level = 0 
for i in range (M):
    temp = list(map(int, input().split()))
    for j in range(N) : 
        if(temp[j] == 1) :
            que.append((i,j,level))
            visited[i][j] = True
    matrix.append(temp)

copy_matrix = [row[:] for row in matrix]

while que :
    item = que.popleft()

    ## level 갱신 
    level = item[2]

    for m in move : 
        next_x = item[0] + m[0]
        next_y = item[1] + m[1]
        
        next_level = item[2] + 1
        ##범위를 벗어난 곳이라면
        if(next_x < 0 or next_y < 0 or next_x >= M or next_y >= N) :
            continue 

        ##이미 방문한 곳이라면 
        if(visited[next_x][next_y]) :
            continue

        ##-1이라면 
        if(matrix[next_x][next_y] == -1) :
            continue

        visited[next_x][next_y] = True
        copy_matrix[next_x][next_y] = 1
        que.append((next_x, next_y, next_level))

for i in range(M) : 
    for j in range(N) :
        if(copy_matrix[i][j] == 0) :
            print(-1)
            exit() 



print(level)
