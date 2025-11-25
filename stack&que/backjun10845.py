import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
que = deque()
output = []

for _ in range(n):
    temp = input().split()

    if temp[0] == "push":
        que.append(int(temp[1]))
    elif temp[0] == "pop":
        output.append(str(que.popleft() if que else -1))
    elif temp[0] == "size":
        output.append(str(len(que)))
    elif temp[0] == "empty":
        output.append("1" if not que else "0")
    elif temp[0] == "front" : # top
        output.append(str(que[0] if que else -1))
    elif temp[0] == "back" :
        output.append(str[que[-1] if que else -1])


print("\n".join(output))
