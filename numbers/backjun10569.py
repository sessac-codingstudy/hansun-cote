import sys
import math 
input = sys.stdin.readline

tc = int(input())
for _ in range(tc) : 
    a,b = map(int,input().split())

    d = a-b 
    print(2 - d)
    