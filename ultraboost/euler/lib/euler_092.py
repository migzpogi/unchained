def square_digits(n):
    sum_digits = 0
    for c in str(n):
        squared = int(c) ** 2
        sum_digits += squared

    return sum_digits


cnt = 0
for i in range(1, 10000000):
    start = i
    while True:
        x = square_digits(start)
        if x == 1:
            break
        if x == 89:
            cnt += 1
            break
        start = x

print(cnt)
