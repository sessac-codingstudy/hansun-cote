import sys

input = sys.stdin.readline

target = int(input())
n = int(input())
temp_arr = list(map(int, input().split()))
n_dict = {}
m_dict = {}

arr_n = []
for t in temp_arr:
    if t not in n_dict:
        n_dict[t] = 1
    else:
        n_dict[t] += 1

arr_n.append(temp_arr[0])
for i in range(1, len(temp_arr)):
    arr_n.append(arr_n[i - 1] + temp_arr[i])

m = int(input())
temp_arr = list(map(int, input().split()))

for t in temp_arr:
    if t not in m_dict:
        m_dict[t] = 1
    else:
        m_dict[t] += 1

arr_m = []
arr_m.append(temp_arr[0])
for i in range(1, len(temp_arr)):
    arr_m.append(arr_m[i - 1] + temp_arr[i])

for i in range(len(arr_n) - 1):
    for j in range(i + 1, len(arr_n)):
        sub_sum = arr_n[j] - (arr_n[i - 1] if i > 0 else 0)
        if sub_sum in n_dict:
            n_dict[sub_sum] += 1
        else:
            n_dict[sub_sum] = 1
for i in range(len(arr_m) - 1):
    for j in range(i + 1, len(arr_m)):
        sub_sum = arr_m[j] - (arr_m[i - 1] if i > 0 else 0)
        if sub_sum in m_dict:
            m_dict[sub_sum] += 1
        else:
            m_dict[sub_sum] = 1

answer = 0
# print(n_dict, m_dict)
for k, v in n_dict.items():
    if target - k in m_dict:
        # print("k t-k ", k, target - k)
        b = m_dict[target - k]
        answer += v * b

print(answer)
