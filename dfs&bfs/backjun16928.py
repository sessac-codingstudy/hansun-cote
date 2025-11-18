백준 16928

import sys 
from collections import deque 
input = sys.stdin.readline
N,M = map(int,input().split())

ladder_dict = {} 
snake_dict= {} 

que = deque()
visited = [False] * 101

for _ in range (N) :
    key,value = map(int,input().split())
    ladder_dict[key] = value 

for _ in range (M) :
    key,value = map(int,input().split())
    snake_dict[key] = value 

## 초기값 입력 (1번째칸, 0단계)
que.append((1,0))

while(que) :
    #아이템 추출, 방문 체크
    top = que.popleft()
    #100이면 break 
    if(top[0] == 100) :
        print(top[1])
        break 
    
    for i in range(1,7) :
    # 다음의 이동할 범위에 사다리 혹은 뱀이있다면 

        next = top[0] + i
        
        #범위 초과 
        if(next > 100) : continue

        #이미 방문한 곳인지
        if(visited[next]) : continue 

        if(next in ladder_dict.keys()) : next = ladder_dict[next]
        elif(next in snake_dict.keys()) :next = snake_dict[next]
    
        que.append((next,top[1] + 1))
        visited[next] = True
        
    

