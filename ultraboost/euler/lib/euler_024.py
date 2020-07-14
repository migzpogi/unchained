import math
import time
from itertools import permutations


def convert_string_to_list(s):
    string_in_list = []
    for c in s:
        string_in_list.append(c)

    return string_in_list


def get_total_number_of_permutations(n, r):
    """
    Returns the total number of permutations
    :param int n: number of objects
    :param int r: taken r at a time
    :return int: number of permutations
    """

    return int(math.factorial(n) / math.factorial(n-r))


def shift_left(s, i):
    if i > 0:
        string_in_list = convert_string_to_list(s)
        a, b = s[i], s[i-1]
        string_in_list[i] = b
        string_in_list[i-1] = a
        return ''.join(string_in_list)
    else:
        return None

y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x = list(permutations(y))
print(x[999999])


# x = 'ABCD'
# loops = get_total_number_of_permutations(4, 4)
# print(loops)
#
# permutations = ['ABCD']
#
# while len(permutations) < loops:
#     for i in reversed(range(0, len(x))):
#         shifted = shift_left(x, i)
#         print(shifted)
#         if shifted:
#             if shifted in permutations:
#                 pass
#             else:
#                 permutations.append(shifted)
#                 x = shifted
#     print(permutations)
#     time.sleep(5)
#