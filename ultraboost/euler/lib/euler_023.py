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


def get_proper_divisors(n):
    return sorted(get_factors(n))[:-1]

def get_status(n):
    total_of_proper_divisors = sum(get_proper_divisors(n))
    if total_of_proper_divisors == n:
        return 0
    elif total_of_proper_divisors < n:
        return -1
    else:
        return 1


print(get_proper_divisors(28))