a, b = map(int, input().split())

# Please write your code here.
count = 0
for i in range(a,b+1) :
    temp = str(i)
    if(i %3 == 0 or '3' in temp or '6' in temp or '9' in temp ) :
        count +=1
print(count)