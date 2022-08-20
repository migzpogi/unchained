from leonhard.leonhard import is_prime

def remarkable(n):
    return (n**2) + n + 41

# print(remarkable(40))
# print(remarkable(41))


def incredible(n, a, b):
    return (n**2) + (a*n) + b

def incredible_prime(a, b, n=0):
    x = incredible(n, a, b)

    if x < 2:
        return None
    else:
        if is_prime(x):
            if n >= 70:
                print(a, b, n)
            incredible_prime(a, b, n+1)
        else:
            return None




# print(is_prime(incredible(1, -79, 1601)))
# print(incredible(2, -79, 1601))
# print(abs(-5))

# a: -999 to 999
# b: -1000 to 1000

a_start = -999
a_end = 999
b_start = -1000
b_end = 1000

# incredible_prime(-999, 1)


for a in range(a_start, a_end+1):
    for b in range(b_start, b_end+1):
        incredible_prime(a, b)

# -59,231
