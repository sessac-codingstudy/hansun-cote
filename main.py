import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
matrix = []
visited = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
    visited.append([False] * m)

x_move = [1,0,-1,0]
y_move = [0,1,0,-1]
que = deque() 

for i in range(n) : 
    for j in range(m) : 
        if(matrix[i][j] == 2) :
            

