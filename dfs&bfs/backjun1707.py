#백준 1707

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):

    V, E = map(int, input().split())

    # 그래프 정보
    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        frm, to = map(int, input().split())
        graph[frm].append(to)
        graph[to].append(frm)

    # 0 = 방문 X, 1 = RED, -1 = BLUE
    color = [0] * (V + 1)

    def bfs(start):
        q = deque()
        q.append(start)
        color[start] = 1  # 시작 색 RED

        while q:
            current = q.popleft()
            next_color = -color[current]

            for nxt in graph[current]:

                # 방문 X → 색 칠하고 큐에 추가
                if color[nxt] == 0:
                    color[nxt] = next_color
                    q.append(nxt)

                # 이미 방문한 노드인데 색이 같으면 이분 그래프 불가
                elif color[nxt] == color[current]:
                    return False

        return True

    answer = True

    # 그래프가 여러 컴포넌트일 수 있어서 모든 정점에서 BFS
    for i in range(1, V + 1):
        if color[i] == 0:   # 아직 방문 못한 노드면 BFS 시작
            if not bfs(i):
                answer = False
                break

    if answer:
        print("YES")
    else:
        print("NO")
