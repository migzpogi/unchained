from leonhard.leonhard import get_factors_of_positive_integer, is_prime


def is_not_prime(n):
    return not is_prime(n)


def remove_one_and_last(n):
    return n[1:-1]



factors = remove_one_and_last(get_factors_of_positive_integer(646))
primes = list(filter(is_prime, factors))
composites = list(filter(is_not_prime, factors))

# print(factors)
# print(primes)
# print(composites)

buffer = []
if composites:
    for c in composites:
        print(c)
        temp = get_factors_of_positive_integer(c)
        print(remove_one_and_last(temp))
        primes.extend(list(filter(is_prime, temp)))
        buffer.extend(list(filter(is_not_prime, temp)))


# x = map(is_prime, y)
#
# for z in x:
#     print(z)