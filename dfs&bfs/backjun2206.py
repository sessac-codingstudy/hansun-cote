백준 2206

import sys 
from collections import deque 
input = sys.stdin.readline
N,M = map(int,input().split())
move_map = [(1,0),(-1,0),(0,1),(0,-1)]
matrix = []
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]


for i in range(N) :
    matrix.append(list(map(int,list(input().strip()))))

def action() :
    que = deque()

    que.append((0,0,0))
    visited[0][0][0] = 1

    while(que) :
        x,y,broken = que.popleft()

        ## 도착지점인지 체크 
        if(x == N-1 and y==M-1) :
            answer = visited[x][y][broken]
            break 

        ## 상하좌우 반복문 
        for move in move_map : 

            #next 다음 이동칸 지정 
            next_row = x + move[0]
            next_col = y + move[1]

            #범위를 넘어가는지 확인 
            if(next_row < 0 or next_col < 0 or next_row > N-1 or next_col > M-1) : 
                continue 

            #다음칸이 빈칸일 경우
            if matrix[next_row][next_col] == 0 and visited[next_row][next_col][broken] == 0 :
                visited[next_row][next_col][broken] == visited[next_row][next_col][broken] + 1 
                que.append((next_row,next_col,broken))

            #다음칸이 벽인데 아직 안 부쉇다면 
            if matrix[next_row][next_col] == 1 and broken == 0 and visited[next_row][next_col][1] == 0 :
                visited[next_row][next_col][1] == visited[next_row][next_col][broken] + 1
                que.append((next_row,next_col,1))
 
    return -1