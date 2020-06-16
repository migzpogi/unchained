"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
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


primes = []
xth_prime = 10001
for i in itertools.count():
    if i == 0 or i == 1:
        continue
    if is_prime(i):
        primes.append(i)
    if len(primes) >= xth_prime:
        print(i)
        break

