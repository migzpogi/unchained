from leonhard.leonhard import count_digits

cnt = 0
for i in range(1, 22):
    for j in range(1, 22):
        x = j**i
        y = count_digits(x)
        if y == i:
            print(j, i, x, y)
            cnt += 1
print(cnt)