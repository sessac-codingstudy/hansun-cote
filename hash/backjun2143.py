import sys
input = sys.stdin.readline

# 처리 과정 
# 1. 가능한 모든 부배열의 합을 dictionary에 저장 
#           1 : 4, 2 : 3 , 3 : 5 ... 

# 2. 두 부 배열의 합이 target이 되는 경우의 수를 찾기 
#     if target = 5 라면 A부배열 합 1 B부배열 합 4 등등 

# 목표 합 T
target = int(input())

# 첫 번째 배열 A
n = int(input())
temp_arr = list(map(int, input().split()))

# 각 부분합의 개수를 저장할 딕셔너리
n_dict = {}
m_dict = {}

# -----------------------
# 배열 A 처리
# -----------------------

# 단일 원소로 이루어진 부분합 개수 세기
for t in temp_arr:
    if t not in n_dict:
        n_dict[t] = 1
    else:
        n_dict[t] += 1

# 누적합 배열 생성
arr_n = []
arr_n.append(temp_arr[0])
for i in range(1, len(temp_arr)):
    arr_n.append(arr_n[i - 1] + temp_arr[i])

# 길이가 2 이상인 모든 부분합 계산
for i in range(len(arr_n) - 1):
    for j in range(i + 1, len(arr_n)):
        # i ~ j 구간 합
        sub_sum = arr_n[j] - (arr_n[i - 1] if i > 0 else 0)
        if sub_sum in n_dict:
            n_dict[sub_sum] += 1
        else:
            n_dict[sub_sum] = 1

# -----------------------
# 배열 B 처리
# -----------------------

m = int(input())
temp_arr = list(map(int, input().split()))

# 단일 원소 부분합
for t in temp_arr:
    if t not in m_dict:
        m_dict[t] = 1
    else:
        m_dict[t] += 1

# 누적합 배열
arr_m = []
arr_m.append(temp_arr[0])
for i in range(1, len(temp_arr)):
    arr_m.append(arr_m[i - 1] + temp_arr[i])

# 모든 부분합 계산
for i in range(len(arr_m) - 1):
    for j in range(i + 1, len(arr_m)):
        sub_sum = arr_m[j] - (arr_m[i - 1] if i > 0 else 0)
        if sub_sum in m_dict:
            m_dict[sub_sum] += 1
        else:
            m_dict[sub_sum] = 1

# -----------------------
# 두 배열 부분합 조합 계산
# -----------------------

answer = 0

# A의 부분합 k와 B의 부분합 (T - k)를 조합
for k, v in n_dict.items():
    if target - k in m_dict:
        # 해당 부분합 조합 개수만큼 더함
        answer += v * m_dict[target - k]

print(answer)
