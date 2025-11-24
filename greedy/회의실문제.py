n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x: (x[1], x[0]))  # 종료시간 기준 정렬

count = 0
last_end = 0

for s, e in arr:
    if s >= last_end:
        count += 1
        last_end = e

print(count)