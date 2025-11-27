def f(n):
    s = 0
    for i in range(0, n, 2):
        for j in range(0, i, 2):
            s += i + j
    return s

print(f(10))