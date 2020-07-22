import itertools
a = [2]
b = [4]
c = [6]
z = []

x = 1001
for i in itertools.count(1):
    if i > x:
        break
    if i % 2 == 0:
        i += 1
        continue
    z.append(i)
    i+=1

y = list(map(lambda m: m**2, z))
# print(y)


n = len(y)

for idx, i in enumerate(range(1, n-1)):
    next_a = c[idx] + 4
    next_b = next_a + 2
    next_c = next_b + 2
    a.append(next_a)
    b.append(next_b)
    c.append(next_c)



d = [1]
e = [1]
f = [1]

for idx, i in enumerate(a):
    next_d = d[idx] + i
    d.append(next_d)

for idx, i in enumerate(b):
    next_e = e[idx] + i
    e.append(next_e)

for idx, i in enumerate(c):
    next_f = f[idx] + i
    f.append(next_f)

# print(d)
# print(e)
# print(f)

diag_sum = (sum(d) + sum(e) + sum(f) + sum(y)) - 3
print(diag_sum)