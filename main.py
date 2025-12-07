import sys
import math

input = sys.stdin.readline

while True:
    temp = list(map(int, input().split()))
    if temp[0] == 0:
        break
    answer_list = []
    nums = temp[1:]

    def nCr(n, ans, r):
        if n == len(nums):
            if len(ans) == r:
                temp = [i for i in ans]
                answer_list.append(temp)
            return
        ans.append(nums[n])
        nCr(n + 1, ans, r)
        ans.pop()
        nCr(n + 1, ans, r)

    nCr(0, [], 6)

    for a in answer_list:
        print(a)
    print()
