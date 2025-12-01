import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

def bfs(start):
    visited = [-1] * (n+1)
    visited[start] = 0
    q = deque([start])

    far_node = start
    max_dist = 0

    while q:
        now = q.popleft()
        for nxt, w in graph[now]:
            if visited[nxt] == -1:
                visited[nxt] = visited[now] + w
                q.append(nxt)
                if visited[nxt] > max_dist:
                    max_dist = visited[nxt]
                    far_node = nxt

    return far_node, max_dist


# 1) 임의 노드(1)에서 가장 멀리 있는 노드 찾기
node_far, _ = bfs(1)

# 2) 그 노드에서 BFS하여 거리 최댓값 = 트리 지름
_, diameter = bfs(node_far)

print(diameter)
