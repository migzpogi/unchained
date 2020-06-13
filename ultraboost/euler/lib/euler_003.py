"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from functools import reduce
import itertools

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


def is_prime(n):

    factors = get_factors(n)
    if len(factors) > 2:
        return False
    else:
        return True

factors_of_n = get_factors(600851475143)
prime_factors_of_n = []
for f in factors_of_n:
    if is_prime(f):
        prime_factors_of_n.append(f)

print(max(prime_factors_of_n))