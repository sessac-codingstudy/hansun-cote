#백준7562

import sys 
from collections import deque

input = sys.stdin.readline

N = int(input())
moving = [
    [1,2],[2,1],[-1,2],[-2,1],[1,-2],[2,-1],[-1,-2],[-2,-1]
]
for _ in range(N) :
    board_range = int(input())
    visited_chess_board = [[False] * board_range for _ in range(board_range)]

    x,y = map(int,input().split())
    tx, ty = map(int,input().split())

    night_que = deque()
    night_que.append([x,y,0])

    answer = 0
    level = 0
    
    # print(x,y,tx,ty)
    while(night_que) :
        #현재 위치
        knight_position = night_que.popleft()
        now_x = knight_position[0]
        now_y = knight_position[1] 
        now_level = knight_position[2]

        if now_x == tx and now_y == ty:
            answer = now_level
            night_que.clear()
            break

        #계층 이동
        #가능한 모든 움직임을 시도 후 큐에 저장 
        for move in moving : 
            ## virtualmove
            vm_x = now_x + move[0]
            vm_y = now_y + move[1] 
            next_level = now_level +1

            # 범위 체크 먼저
            if vm_x < 0 or vm_y < 0 or vm_x >= board_range or vm_y >= board_range:
                continue
            
            # 방문 체크 먼저
            if visited_chess_board[vm_x][vm_y]:
                continue
            
            visited_chess_board[vm_x][vm_y] = True

            night_que.append([vm_x,vm_y, next_level])

    print(answer)


