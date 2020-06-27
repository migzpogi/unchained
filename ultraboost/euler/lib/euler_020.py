def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    return n


def sum_digits(n):
    total = 0
    for i in str(n):
        total += int(i)

    return total


f = factorial(100)
print(sum_digits(f))