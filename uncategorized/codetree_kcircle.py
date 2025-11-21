
m collections import deque 

n, k = map(int, input().split())

# Please write your code here.
q = deque() 
for i in range(1,n+1) :
        q.append(i)

        while(len(q) > 0) :
                for i in range(k-1) :
                            t = q.popleft()
                                    q.append(t)
                                        
                                            print(q.popleft(),end =' ')
