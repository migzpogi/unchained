from leonhard.leonhard import get_factors_of_positive_integer, is_prime


def remove_one_and_last(n):
    return n[1:-2]

y = get_factors_of_positive_integer(646)


print(remove_one_and_last(y))
# x = map(is_prime, y)
#
# for z in x:
#     print(z)