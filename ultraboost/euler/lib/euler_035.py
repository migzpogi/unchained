from leonhard.leonhard import is_prime
from itertools import permutations


def num_to_iter(n):
    num_iter = []
    for i in str(n):
        num_iter.append(i)

    return num_iter


def iter_to_num(i):
    num_iter = []
    for j in i:
        num_iter.append(int("".join(j)))
    return num_iter



circular_primes = []
for i in range(1, 10001):
    if i == 1:
        continue
    if not is_prime(i):
        continue

    circular = iter_to_num(list(set(permutations(num_to_iter(i)))))
    print(i)
    print(circular)
    true_circular = list(filter(is_prime, circular))
    print(true_circular)
    if len(circular) == len(true_circular):
        circular_primes.append(i)

print(circular_primes)
