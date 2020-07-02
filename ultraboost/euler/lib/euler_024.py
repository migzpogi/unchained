import math

"""
0123
0132
0213
0231
0312
0321


"""


def get_total_number_of_permutations(n, r):
    """
    Returns the total number of permutations
    :param int n: number of objects
    :param int r: taken r at a time
    :return int: number of permutations
    """

    return int(math.factorial(n) / math.factorial(n-r))


print(get_total_number_of_permutations(4, 4))