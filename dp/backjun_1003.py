import sys

input = sys.stdin.readline
n = int(input())
dp = []
dp.append((1, 0))
dp.append((0, 1))
dp.append((1, 1))


def func(num):
    if num <= 2:
        return dp[num]
    for i in range(3, num + 1):
        a, b = dp[-1]
        c, d = dp[-2]
        dp.append((a + c, b + d))
    return dp[num]


for i in range(n):
    d1, d2 = func(int(input()))
    print(d1, d2)
