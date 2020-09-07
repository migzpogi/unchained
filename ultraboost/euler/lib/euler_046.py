from leonhard.leonhard import is_prime
import itertools


def twice_square(n):
    return 2 * (n**2)


for n in itertools.count(1):
    if n % 2 == 0:
        continue
    if not is_prime(n):
        for i in itertools.count(1):
            x = twice_square(i)
            if x < n:
                if is_prime(n-x):
                    # print(f"{n} = {n-x} + (2 x ({i ** 2}))")
                    break
            else:
                print(n)
                break