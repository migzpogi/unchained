rows = []
with open('triangle_0.txt', 'r') as f:
    for lines in f.readlines():
        rows.append(lines.strip().split(' '))

print(rows)

r1 = [3]
r2 = [7, 4]
r3 = [2, 4, 6]
r4 = [8, 5, 3, 9]
rr = [r1, r2, r3]


def adjacent(i, row):
    return row[i], row[i+1]

# temp = []
# for idx_main, i in enumerate(rr):
#     for idx, j in enumerate(i):
#         a = adjacent(idx, rr[idx_main+1])
#         print(j, a[0])
#         print(j, a[1])


def get_adjacent(row, next_row, total_row):
    for i, r in enumerate(row):
        if total_row:
            temp = []
            total_row.append([total_row[i], next_row[i]])
            total_row.append([total_row[i], next_row[i + 1]])
            print(total_row)
        else:
            total_row.append([r, next_row[i]])
            total_row.append([r, next_row[i+1]])
            print(total_row)

a = []
get_adjacent(r1, r2, a)
get_adjacent(r2, r3, a)