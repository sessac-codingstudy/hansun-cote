nt(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

# Please write your code here.
set_a = set(a)
for i in b :
        if i in set_a :
                    print(1)
                        else :
                                    print(0)
