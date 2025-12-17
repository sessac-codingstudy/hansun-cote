import sys
import math 
input = sys.stdin.readline

d,a,b = map(int,input().split())
diagonal = d * d 
a2 = a * a 
b2 = b *b 
height = diagonal * (a2 / (a2+b2))
width = diagonal * (b2 / (a2+b2))
print(f"{math.sqrt(height) // 1:.0f} {math.sqrt(width) // 1:.0f}")
