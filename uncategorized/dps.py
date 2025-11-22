n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

moves = [[1,0],[-1,0],[0,1],[0,-1]]
# Please write your code here.
def dfs(row,col) :
        
        if(grid[row][col] == 0) :
                    return 0

                    stk = []
                        count = 0
                            stk.append((row,col))

                                while stk :
                                            x,y = stk.pop()
                                                    if(grid[x][y] == 0) : continue 
                                                            grid[x][y] = 0
                                                                    count +=1

                                                                            for move in moves  :
                                                                                            next_x, next_y = x+move[0], y+move[1] 
                                                                                                        
                                                                                                                    if(next_x < 0 or next_y < 0 or next_x >= n or next_y >= n) :
                                                                                                                                        continue

                                                                                                                                                if(grid[next_x][next_y] != 0) : 
                                                                                                                                                                    stk.append((next_x,next_y))

                                                                                                                                                                            
                                                                                                                                                                                
                                                                                                                                                                                    return count 

                                                                                                                                                                                town_count = 0 
                                                                                                                                                                                town_lst = []
                                                                                                                                                                                for i in range(n) :
                                                                                                                                                                                        for j in range(n) :
                                                                                                                                                                                                    val = dfs(i,j)
                                                                                                                                                                                                            if(val != 0) :
                                                                                                                                                                                                                            town_count +=1 
                                                                                                                                                                                                                                        town_lst.append(val)

                                                                                                                                                                                                                                        town_lst.sort()
                                                                                                                                                                                                                                        print(town_count)
                                                                                                                                                                                                                                        for i in town_lst :
                                                                                                                                                                                                                                                print(i)

