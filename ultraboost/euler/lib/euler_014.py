next_collatz = lambda n: int(n/2) if n % 2 == 0 else (3*n) + 1


def chain(x, elem):
    elem.append(x)
    y = next_collatz(x)
    if y != 1:
        chain(y, elem)

    return elem


chain_len = []
for i in range(1, 1000000):
    elem = []
    chain_len.append(len(chain(i, elem)))


longest = max(chain_len)
print(longest)
print(chain_len.index(longest)+1)