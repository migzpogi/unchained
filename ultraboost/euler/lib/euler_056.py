def raise_to(a, b):
    return a**b


def digital_sum(n):
    total = 0
    for c in str(n):
        total += int(c)

    return total


# x = raise_to(3, 10)
# print(x, digital_sum(x))

list_of_sums = []
for i in range(1, 100):
    for j in range(1, 100):
        x = raise_to(i, j)
        y = digital_sum(x)
        list_of_sums.append(y)

print(max(list_of_sums))