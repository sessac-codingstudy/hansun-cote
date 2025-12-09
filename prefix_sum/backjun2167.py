import sys 

input = sys.stdin.readline 

n,m = map(int,input().split())
matrix = []
for _ in range(n) : 
    matrix.append(list(map(int,input().split())))

test_case = []
tc = int(input())
for _ in range(tc) : 
    test_case.append(list(map(int,input().split())))

for i in range(m-1) :
    matrix[0][i+1] = matrix[0][i] + matrix[0][i+1]

for j in range(n-1) : 
    matrix[j+1][0] = matrix[j+1][0] + matrix[j][0]
# print(matrix)

for i in range(1,n) : 
    for j in range(1,m) :
        matrix[i][j] = matrix[i][j] + matrix[i-1][j] + matrix[i][j-1] - matrix[i-1][j-1]


# 구간합 처리
for row1, col1, row2, col2 in test_case:
    r1, c1 = row1-1, col1-1
    r2, c2 = row2-1, col2-1

    result = matrix[r2][c2]
    if r1 > 0:
        result -= matrix[r1-1][c2]
    if c1 > 0:
        result -= matrix[r2][c1-1]
    if r1 > 0 and c1 > 0:
        result += matrix[r1-1][c1-1]

    print(result)