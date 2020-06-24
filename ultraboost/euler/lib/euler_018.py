rows = []
with open('triangle_0.txt', 'r') as f:
    for lines in f.readlines():
        rows.append(lines.strip().split(' '))

print(rows)

r1 = [3]
r2 = [7, 4]
r3 = [2, 4, 6]
r4 = [8, 5, 3, 9]
rr = [r1, r2, r3, r4]

