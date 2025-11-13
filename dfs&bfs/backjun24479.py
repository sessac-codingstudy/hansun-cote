import sys 
input = sys.stdin.readline

N, M, R = map(int,input().split())
visited = [False] * (N+1)
first_visited = [0] * (N+1)
stk = []

mapping = {}
for i in range(1,N+1) :
    mapping[i] = []
for i in range(M) :
    frm, to = map(int,input().split())
    mapping[frm].append(to) 
    mapping[to].append(frm) 

for i in range (1,N+1) :
    mapping[i].sort()
stk = [R]
order = 0 

while (len(stk) > 0) :
    top = stk.pop()
    if(visited[top] == True) :
        continue 
    
    visited[top] = True
    order +=1
    first_visited[top] = order 

    for node in mapping[top] :
        if(visited[node] == False) :
            stk.append(node)
        
for p in range(1,len(first_visited)):
    print(first_visited[p])