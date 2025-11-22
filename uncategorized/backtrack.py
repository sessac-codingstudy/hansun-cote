n = int(input())

series = ["1","22","333","4444"]
# Please write your code here.

count = 0
def backtrack(now_numbers) :
        global count 
            
                if(len(now_numbers) > n) :
                            return 
                            elif(len(now_numbers) == n) :
                                        count += 1

                                            for s in series :
                                                        backtrack(now_numbers + s)

                                                        backtrack("")
                                                        print(count)
