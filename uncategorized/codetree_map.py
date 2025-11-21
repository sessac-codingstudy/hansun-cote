n, k = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
visited = {}

# 등장 횟수 기록
for x in arr:
        visited[x] = visited.get(x, 0) + 1

        answer = 0

        for key in visited:
                alter = k - key

                    # 존재하지 않으면 패스
                        if alter not in visited:
                                    continue

                                    if key == alter:   # 같은 수로 조합 만드는 경우
                                                cnt = visited[key]
                                                        answer += cnt * (cnt - 1) // 2
                                                            elif key < alter:  # 중복 방지 위해 key < alter
                                                                        answer += visited[key] * visited[alter]

                                                                        print(answer)

