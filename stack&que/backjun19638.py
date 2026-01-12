import sys
import heapq

input = sys.stdin.readline

# n : 거인의 수
# centy : 센티의 키
# t : 망치를 사용할 수 있는 최대 횟수
n, centy, t = map(int, input().split())

# 파이썬 heapq는 최소 힙이므로
# 음수로 저장해서 최대 힙처럼 사용
hq = []
for _ in range(n):
    heapq.heappush(hq, -int(input()))

# 센티가 이겼는지 여부
success = False

# 망치를 최대 t번 사용
for i in range(t):
    # 현재 가장 큰 거인 키 꺼내기
    tallest = -heapq.heappop(hq)

    # 이미 센티보다 작다면 성공
    if tallest < centy:
        success = True
        print("YES")
        print(i)  # 사용한 망치 횟수
        break

    # 키가 1이면 더 줄어들지 않음 (문제 조건)
    if tallest == 1:
        heapq.heappush(hq, -1)
        continue

    # 망치 사용 → 키를 절반으로 (정수 나눗셈)
    tallest //= 2

    # 다시 힙에 넣기
    heapq.heappush(hq, -tallest)

# 망치를 다 사용한 후에도 성공하지 못한 경우
if not success:
    tallest = -heapq.heappop(hq)

    # 마지막 상태에서 센티보다 작아졌다면 성공
    if tallest < centy:
        print("YES")
        print(t)
    else:
        # 끝까지 못 줄인 경우
        print("NO")
        print(tallest)
