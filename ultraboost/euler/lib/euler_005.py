"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
232792560
"""

def check_divisors(x, divisors):
    for d in divisors:
        if x % d != 0:
            return False

    return True


divisors = range(1, 21)
x = 1

while not check_divisors(x, divisors):
    x += 1

print(x)