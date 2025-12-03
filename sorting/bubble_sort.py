n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for i in range(0,n) :
  for j in range(0,n-i-1) :
    if(arr[j] > arr[j+1]) :
      arr[j], arr[j+1] = arr[j+1], arr[j]

for i in arr :
  print(i,end=' ')
