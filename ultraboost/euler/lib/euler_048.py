def raise_to_self(n):
    return n**n

total = 0
for i in range(1, 1001):
    total += raise_to_self(i)

print(total)