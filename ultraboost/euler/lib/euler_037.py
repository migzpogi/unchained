import itertools
from leonhard.leonhard import is_prime


def remove_left(n):
    return n[1:]


def remove_right(n):
    return n[:-1]


def is_truncatable_left(n):
    loop_count = len(str(n))
    x = str(n)
    while loop_count != 0:
        if is_prime(int(x)):
            if loop_count > 1:
                x = remove_left(x)
            else:
                return True
        else:
            return False
        loop_count -= 1


def is_truncatable_right(n):
    loop_count = len(str(n))
    x = str(n)
    while loop_count != 0:
        if is_prime(int(x)):
            if loop_count > 1:
                x = remove_right(x)
            else:
                return True
        else:
            return False
        loop_count -= 1

skip = [2, 3, 5, 7]
skip_2 = [0, 2, 4, 6, 8]
trunc_list = []
for i in itertools.count(1):
    if i in skip:
        continue
    if str(i)[-1] in skip_2:
        continue
    if is_truncatable_left(i) and is_truncatable_right(i):
        trunc_list.append(i)
    if len(trunc_list) == 11:
        break

print(sum(trunc_list))

