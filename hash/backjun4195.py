import sys 
input = sys.stdin.readline

tc = int(input())

def solution() : 
  count = int(input())
  friend_dict = {} 
  for _ in range(count) :
    f1, f2 = input().split() 
    if f1 not in friend_dict : 
      friend_dict[f1] = set([f2])
    else : 
      friend_dict[f1].add(f2)

    if f2 not in friend_dict : 
      friend_dict[f2] = set([f1])
    else :
      friend_dict[f2].add(f1)
  print(friend_dict)

for _ in range(tc) : 
  solution()