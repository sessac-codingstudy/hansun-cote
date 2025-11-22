n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

# Please write your code here.
import bisect 
for q in queries :
        index = bisect.bisect_left(arr,q)
            if(index < len(arr) and arr[index] == q) :
                        print(index+1)
                            else :
                                        print(-1)

