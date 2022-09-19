from fractions import Fraction
import time

def get_hcf(x, y):
    """
    Gets the highest common factor
    """

    if x > y:
        smaller = x
    else:
        smaller = y

    for i in range(1, smaller+1):
        if x%i == 0 and y%i == 0:
            hcf = i

    return hcf

def is_hcf_one(n, d):
    if get_hcf(n, d) == 1:
        return True
    else:
        return False


start = time.time()

# x = 5001
# list_of_fractions = []
#
# for d in range(1, x+1):
#     if d%10000 == 0:
#         print(f"Processing: {d}")
#     for n in range(1, d):
#         # if n%2 == 0 and d%2 == 0:
#         #     continue
#         # if d%n == 0 and n != 1:
#         #     continue
#
#         if n < d and is_hcf_one(n, d):
#             y = Fraction(n, d)
#             list_of_fractions.append(y)
#
# s = sorted(list_of_fractions)
#
# for idx, i in enumerate(s):
#     if i == Fraction(3, 7):
#         print(s[idx-1])

x = Fraction(3, 8)
y = Fraction(2, 5)



cnt = 0
a = 0.000000000000001
b = 0.428571428571428
d = 0.428571300000001
z = Fraction(d).limit_denominator(1000000)
print(z)

# while True:
#     c = b-a
#
#     if cnt%200000 == 0:
#         print(f"Processing: {c}")
#
#     z = Fraction(c).limit_denominator(1000000)
#
#     if z != Fraction(3, 7):
#         print(f"Answer: {c} {z}")
#         break
#
#     b = c
#     cnt += 1



end = time.time()
print(end-start)