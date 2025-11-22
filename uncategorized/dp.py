n = int(input())

# Please write your code here.
# 2x1 크기 1 
# 2x2 크기 2
# 2x3 크기 3
# 2x4 크기 5
# 2x5 크기 6 
def func(n) :
        if(n==1) : return 1
            elif(n == 2) : return 2 
                df = [0] * (n+1) 
                    df[0] = 1
                        df[1] = 2
                            cnt = 2 
                                while(cnt < n) :
                                            df[cnt] = df[cnt-1] + df[cnt-2]
                                                    cnt +=1 
                                                        
                                                            print(df[cnt-1] % 10007)

                                                            func(n)

