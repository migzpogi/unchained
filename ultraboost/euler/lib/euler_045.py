import itertools


def generate_triangle_sequence(n):
    return (n+1) * n * 0.5


def is_triangular(n):
    if (((8*n) + 1)**0.5) % 1 == 0:
        return True
    else:
        return False


def is_pentagonal(n):
    if (((((24 * n) + 1) ** 0.5) + 1) / 6) % 1 == 0 :
        return True
    else:
        return False


def is_hexagonal(n):
    if (((((8 * n) + 1) ** 0.5) + 1) / 4) % 1 == 0 :
        return True
    else:
        return False

skip = [1, 40755]
for i in itertools.count():
    triangle = generate_triangle_sequence(i)
    if triangle not in skip and is_pentagonal(triangle) and is_hexagonal(triangle):
        print(triangle)
        break
