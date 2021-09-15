import math
from leonhard.leonhard import get_factors_of_positive_integer


numbers = []

with open("p099_base_exp.txt", "r") as f:
    for idx, lines in enumerate(f.readlines()):
        numbers.append((idx, lines.strip()))



# a= [1, 2, 3]
# print(a)
# b = a.pop(0)
# print(b)
# print(a)

# """
# 2**5 = 32 == log(32, 2) = 5
# """
# a = 2
# b = 5
#
# print(a**b) # 32
# print(math.log(32, 2)) # 5
#
# b1 = 2
# e1 = 2000
# b2 = 10
# e2 = 800
#
# gcd = math.gcd(e1, e2)
#
# x1 = e1/gcd
# x2 = e2/gcd
#
# print(f"{b1}^{x1}^{gcd}")
# print(f"{b2}^{x2}^{gcd}")
#

def compare_numbers(num1, num2):
    print(f"Comparing {num1} and {num2}")
    idx_1 = num1[0]
    idx_2 = num2[0]

    base_1 = int(num1[1].split(",")[0])
    base_2 = int(num2[1].split(",")[0])

    exp_1 = int(num1[1].split(",")[1])
    exp_2 = int(num2[1].split(",")[1])

    gcd = math.gcd(exp_1, exp_2)

    x_1 = int(exp_1/gcd)
    x_2 = int(exp_2/gcd)

    if base_1**x_1 > base_2**x_2:
        return (idx_1, f"{base_1},{exp_1}")
    else:
        return (idx_2, f"{base_2},{exp_2}")


highest = None

# numbers = [
#     (0, '519432,525806'),
#     (1, '632382,518061'),
#     (2, '78864,613712')
# ]

while(numbers):
    current = numbers.pop(0)

    if highest is None:
        highest = current
        print(f"Current highest: {highest}")
        continue

    highest = compare_numbers(current, highest)
    print(f"Current highest: {highest}")


print(f"Final highest: {highest}")