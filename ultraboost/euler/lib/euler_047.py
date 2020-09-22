import itertools
from leonhard.leonhard import get_factors_of_positive_integer, is_prime


def is_not_prime(n):
    return not is_prime(n)


def remove_one_and_last(n):
    return n[1:-1]

# buffer = []
# factors = remove_one_and_last(get_factors_of_positive_integer(14))
# print(factors)
#
# for f in factors:
#     if is_prime(f):
#         buffer.append(f)
#     else:
#         buffer.extend(remove_one_and_last(get_factors_of_positive_integer(f)))

distinct = 3
streak_limit = 4
consecutive = []
streak = 0
for i in itertools.count(646):
    if is_prime(i):
        consecutive = []
        streak = 0
        continue
    # if i == 650:
    #     break
    factors = remove_one_and_last(get_factors_of_positive_integer(i))
    if len(factors) > distinct:
        print(i, factors)
        consecutive.append(i)
        streak += 1
        if streak == streak_limit:
            break
    else:
        consecutive = []
        streak = 0

print(consecutive)



# print(buffer)
# primes = list(filter(is_prime, factors))
# composites = list(filter(is_not_prime, factors))
#
# # print(factors)
# # print(primes)
# # print(composites)
#
# buffer = []
# if composites:
#     for c in composites:
#         print(c)
#         temp = get_factors_of_positive_integer(c)
#         print(remove_one_and_last(temp))
#         primes.extend(list(filter(is_prime, temp)))
#         buffer.extend(list(filter(is_not_prime, temp)))
#
#
#
#
# # x = map(is_prime, y)
# #
# # for z in x:
# #     print(z)