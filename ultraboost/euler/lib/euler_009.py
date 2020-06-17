def is_triplet(a, b, c):
    if a < b < c:
        if ((a**2) + (b**2)) == c**2:
            return True
        else:
            return False
    else:
        return False


total = 1000

for x in range(1, total-1):
    for y in range(1, total-x):
        z = total-y-x
        if is_triplet(x, y, z):
            print(x, y, z)
            print(x*y*z)