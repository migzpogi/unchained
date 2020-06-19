row_1 = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08".split(" ")
row_2 = "49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00".split(" ")
row_3 = "81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65".split(" ")
row_4 = "52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91".split(" ")
row_5 = "22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80".split(" ")
row_6 = "24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50".split(" ")
row_7 = "32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70".split(" ")
row_8 = "67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21".split(" ")
row_9 = "24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72".split(" ")
row_10 = "21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95".split(" ")
row_11 = "78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92".split(" ")
row_12 = "16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57".split(" ")
row_13 = "86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58".split(" ")
row_14 = "19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40".split(" ")
row_15 = "04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66".split(" ")
row_16 = "88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69".split(" ")
row_17 = "04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36".split(" ")
row_18 = "20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16".split(" ")
row_19 = "20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54".split(" ")
row_20 = "01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48".split(" ")


def get_product(adjacent):
    product = 1
    for a in adjacent:
        product *= int(a)

    return product


def translate_columns_to_rows(*args):
    columns = []
    i = 0
    while i < len(args[0]):
        j = 0
        temp_list = []
        while j < len(args):
            temp_list.append(args[j][i])
            j += 1
        columns.append(temp_list)
        i += 1

    return columns


def get_adjacent_horizontal(row, n):
    adjacent_numbers = []
    i = 0
    while n <= len(row):
        adjacent_numbers.append(row[i:n])
        i += 1
        n += 1

    return adjacent_numbers


def get_diag_right(*args):
    diag_right_list = []
    for i, a in enumerate(args):
        for j, n in enumerate(a):
            temp_list = []
            try:
                temp_list.append(n)
                temp_list.append(args[i+1][j+1])
                temp_list.append(args[i+2][j+2])
                temp_list.append(args[i+3][j+3])
            except:
                temp_list = []
                pass
            if temp_list:
                diag_right_list.append(temp_list)

    return diag_right_list


def get_diag_left(*args):
    diag_left_list = []
    for i, a in enumerate(args):
        for j, n in enumerate(a):
            temp_list = []
            try:
                if j-1 < 0 or j-2 < 0 or j-3 < 0:
                    continue
                temp_list.append(n)
                temp_list.append(args[i+1][j-1])
                temp_list.append(args[i+2][j-2])
                temp_list.append(args[i+3][j-3])
            except:
                temp_list = []
                pass
            if temp_list:
                diag_left_list.append(temp_list)

    return diag_left_list

rows = [row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9, row_10,
        row_11, row_12, row_13, row_14, row_15, row_16, row_17, row_18, row_19, row_20]

products = []

# horizontal
for r in rows:
    adjacent_row = get_adjacent_horizontal(r, 4)
    for ar in adjacent_row:
        product = get_product(ar)
        products.append(product)

        # print(f'{ar} | {product}')

# vertical
columns = translate_columns_to_rows(row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9, row_10,
        row_11, row_12, row_13, row_14, row_15, row_16, row_17, row_18, row_19, row_20)
for c in columns:
    adjacent_col = get_adjacent_horizontal(c, 4)
    for ac in adjacent_col:
        product = get_product(ac)
        products.append(product)

        # print(f'{ac} | {product}')

# diag right
diag_right = get_diag_right(row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9, row_10,
        row_11, row_12, row_13, row_14, row_15, row_16, row_17, row_18, row_19, row_20)
for dr in diag_right:
    product = get_product(dr)
    products.append(product)

    # print(f'{dr} | {product}')

# diag left
diag_left = get_diag_left(row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9, row_10,
        row_11, row_12, row_13, row_14, row_15, row_16, row_17, row_18, row_19, row_20)
for dl in diag_left:
    product = get_product(dl)
    products.append(product)

    # print(f'{dl} | {product}')

print(max(products))




