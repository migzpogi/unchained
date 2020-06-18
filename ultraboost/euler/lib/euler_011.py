row_1 = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08".split(" ")
row_2 = "49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00".split(" ")
row_3 = "81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65".split(" ")


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

translate_columns_to_rows(row_1, row_2, row_3)



