from functools import reduce
from leonhard.leonhard import get_factors_of_positive_integer
from leonhard.leonhard import is_prime

def get_proper_divisors(n):
    return get_factors_of_positive_integer(n)[:-1]


def get_status(n):
    total_of_proper_divisors = sum(get_proper_divisors(n))
    if total_of_proper_divisors == n:
        return 0
    elif total_of_proper_divisors < n:
        return -1
    else:
        return 1

limit = 28123
abundant_numbers = []
for i in range(1, limit):
    if get_status(i) == 1:
        abundant_numbers.append(i)

# print(abundant_numbers)

sum_of_abundant_numbers = []
for j in abundant_numbers:
    sum_of_abundant_numbers.extend(list(map(lambda x: x+j if x+j < limit else None, abundant_numbers)))

all_sum_abundant = list(set(sum_of_abundant_numbers))

not_abundant = []
for k in range(1, limit):
    if k not in all_sum_abundant:
        not_abundant.append(k)

# print(not_abundant)
print(sum(not_abundant))