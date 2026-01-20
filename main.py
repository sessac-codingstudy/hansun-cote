def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

# 무한 루프에 빠지지 않고, 필요할 때만 번호를 하나씩 따올 수 있음
gen = infinite_sequence()
print(next(gen)) # 0
print(next(gen)) # 1
# ... 계속해서 호출 가능