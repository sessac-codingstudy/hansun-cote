n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
min_value = 1000000000000
for i in range(n):
    sum_v = 0
    for j in range(n):
        sum_v += A[j] * abs(i - j)
    min_value = min(min_value, sum_v)
print(min_value)
