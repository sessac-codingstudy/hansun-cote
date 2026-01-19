import sys 
input = sys.stdin.readline 

# -------------------------------------------------
# 입력 처리
# -------------------------------------------------
n = int(input())              # 영상의 크기 (n x n)
matrix = []                   # 흑백 영상 저장

for _ in range(n):
    temp = []
    # 한 줄이 "0101" 같은 문자열이므로 문자 하나씩 처리
    for t in input().strip():
        temp.append(int(t))   # '0' or '1' → int 변환
    matrix.append(temp)

# -------------------------------------------------
# 특정 영역이 모두 같은 값인지 확인하는 함수
# -------------------------------------------------
def check_matrix(left_x, left_y, right_x, right_y):
    """
    (left_x, left_y)부터 (right_x, right_y) 직전까지의 영역이
    모두 같은 값이면 해당 값(0 또는 1) 반환
    하나라도 다르면 -1 반환
    """
    global matrix

    init_value = matrix[left_x][left_y]  # 기준 값

    for i in range(left_x, right_x):
        for j in range(left_y, right_y):
            if matrix[i][j] != init_value:
                return -1                # 다른 값 발견 → 분할 필요
    return init_value                    # 전부 동일

# -------------------------------------------------
# 쿼드트리 결과를 저장할 리스트
# -------------------------------------------------
answer_list = []

# -------------------------------------------------
# 분할 정복(재귀) 함수
# -------------------------------------------------
def recur(left_x, left_y, right_x, right_y):
    global answer_list

    # 현재 영역이 단색인지 검사
    result = check_matrix(left_x, left_y, right_x, right_y)

    # 단색이면 바로 결과에 추가
    if result != -1:
        answer_list.append(result)
    else:
        # 단색이 아니면 4분할
        mid_x = (right_x + left_x) // 2
        mid_y = (right_y + left_y) // 2

        answer_list.append("(")          # 분할 시작 표시

        # 왼쪽 위
        recur(left_x, left_y, mid_x, mid_y)
        # 오른쪽 위
        recur(left_x, mid_y, mid_x, right_y)
        # 왼쪽 아래
        recur(mid_x, left_y, right_x, mid_y)
        # 오른쪽 아래
        recur(mid_x, mid_y, right_x, right_y)

        answer_list.append(")")          # 분할 종료 표시

# -------------------------------------------------
# 전체 영역부터 시작
# -------------------------------------------------
recur(0, 0, n, n)

# -------------------------------------------------
# 결과 출력
# -------------------------------------------------
string = ""
for s in answer_list:
    string += str(s)

print(string)
