from functools import reduce


def get_factors(n):

    if n == 0:
        return 0

    ## this is the "mid point" factor of a number. if n = 25, the midpoint is 5 (1,5,5,25). stop there.
    midpoint = int(n**0.5)

    ## loops through 1 to midpoint, if n % factor == 0 then it means it is a divisor
    ## we get that and also the n//factor
    list_of_factors = ([factor, n//factor] for factor in range(1, midpoint+1) if n % factor == 0)

    ## we combine all list_of_factors
    total_factors = reduce((lambda a, b: a+b), list_of_factors)

    return total_factors


def d_n(n):
    factors = get_factors(n)
    factors.sort()
    factors = factors[0:-1]
    total = 0
    for f in factors:
        total += f
    return total


def is_amicable(a):
    b = d_n(a)
    if a == d_n(b) and a != b:
        return True
    else:
        return False


amicable = []

for i in range(1, 10001):
    if is_amicable(i):
        amicable.append(i)

print(sum(amicable))
