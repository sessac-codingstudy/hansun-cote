#백준 24444

import sys 
input = sys.stdin.readline

N, M, R = map(int,input().split())
visited = [False] * (N+1)

## 각 노드별 방문 순서 
## i번째 노드는 first_visited[i] 번째로 방문한다 

first_visited = [0] * (N+1)
que = []

mapping = {}
for i in range(1,N+1) :
    mapping[i] = []
for i in range(M) :
    frm, to = map(int,input().split())
    mapping[frm].append(to) 
    mapping[to].append(frm) 

for i in range (1,N+1) :
    mapping[i].sort() ## 인접 정점을 오름차순으로 방문 하기 때문 

que = [R]
order = 0 # 방문 순서 

while (len(que) > 0) :
    top = que.pop(0)
    if(visited[top] == True) :
        continue 
    
    visited[top] = True
    order +=1
    first_visited[top] = order 

    ## node에서 방문할 수 있는 모든 node 
    for node in mapping[top] :
        if(visited[node] == False) :
            que.append(node)
        
for p in range(1,len(first_visited)):
    print(first_visited[p])