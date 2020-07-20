import math

def get_longest_repeating(denominator):
    remainders = []
    quotients = []

    x = 1
    y = denominator
    while True:
        r = x%y

        if r not in remainders:
            remainders.append(r)
            q = math.floor(x / y)
            quotients.append(q)
            x = r*10
        else:
            break

    return len(remainders)

z = [0]
for i in range(1, 1001):
    z.append(get_longest_repeating(i))

max_repeat = max(z)
print(z.index(max_repeat))