from fractions import Fraction

def get_hcf(x, y):
    """
    Gets the highest common factor
    """

    if x > y:
        smaller = x
    else:
        smaller = y

    for i in range(1, smaller+1):
        if x%i == 0 and y%i == 0:
            hcf = i

    return hcf


print(get_hcf(54, 24))
