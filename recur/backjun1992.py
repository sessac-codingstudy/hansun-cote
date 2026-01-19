import sys 
input = sys.stdin.readline 

n = int(input())
matrix = [] 
for _ in range(n) : 
    temp = [] 
    for t in input().strip() :
        temp.append(int(t))
    matrix.append(temp)

def check_matrix(left_x, left_y, right_x, right_y) : 
    global matrix 

    init_value = matrix[left_x][left_y]
    for i in range(left_x, right_x) :
        for j in range(left_y, right_y) :
            if(matrix[i][j] != init_value) : return -1
            # print(matrix[j][i],end=' ')
        # print()
    return init_value
answer_list = []    
def recur(left_x, left_y, right_x, right_y) :
    # print(left_x, left_y)
    global answer_list
    result = check_matrix(left_x,left_y,right_x,right_y)
    
    if result != -1 : 
        answer_list.append(result)
    else : 
        mid_x = (right_x + left_x) // 2
        mid_y = (right_y + left_y) // 2
        answer_list.append("(")
        recur(left_x, left_y, mid_x, mid_y)
        recur(left_x,mid_y,mid_x, right_y)
        recur(mid_x,left_y,right_x,mid_y)
        recur(mid_x,mid_y, right_x, right_y)
        answer_list.append(")")

recur(0,0,n,n)

string = ""
for s in answer_list :
    string += str(s)
print(string)