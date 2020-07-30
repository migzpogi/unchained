from leonhard.leonhard import is_prime
from itertools import permutations
from collections import deque


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

even = [0, 2, 4, 6, 8]
circular_primes = []
for i in range(1, 1000001):
    if i == 1:
        continue
    if i == 2:
        circular_primes.append(i)
    if int(str(i)[-1]) in even:
        continue
    if not is_prime(i):
        continue

    num_iter = deque(num_to_iter(i))
    buffer = []
    for j in range(len(num_iter)):
        buffer.append(list(num_iter))
        num_iter.rotate(1)
    circular = iter_to_num(buffer)
    true_circular = list(filter(is_prime, circular))

    if len(circular) == len(true_circular):
        circular_primes.append(i)


    # circular = iter_to_num(list(set(permutations(num_to_iter(i)))))
    # print(i)
    # print(circular)
    # true_circular = list(filter(is_prime, circular))
    # print(true_circular)
    # if len(circular) == len(true_circular):
    #     circular_primes.append(i)

# print(circular_primes)
print(len(circular_primes))