import sys
import math 
input = sys.stdin.readline

from itertools import combinations
n,k = map(int,input().split())

ans = int(math.factorial(n)//(math.factorial(k)*math.factorial(n-k)))
print(ans % 10007)