champ = "."
prod = 1
x = [1, 10, 100, 1000, 10000, 100000, 1000000]

for i in range(1, 1000001):
    champ += str(i)
    if i in x:
        print(champ[i])
        prod *= int(champ[i])

print(prod)
