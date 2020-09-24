from itertools import permutations, count


def int_to_list(n):
    x = []
    for c in str(n):
        x.append(c)
    return x


def get_list_of_perms(n):
    x = permutations(n)
    y = []
    for i in x:
        y.append(int("".join(list(i))))
    return y


# a = 125874
# b = 2*a
# c = get_list_of_perms(int_to_list(a))
# if b in c:
#     print("found")

for i in count(2):
    two = 2*i
    three = 3*i
    four = 4*i
    five = 5*i
    six = 6*i
    perms = get_list_of_perms(int_to_list(i))
    if two in perms and three in perms and four in perms and five in perms and six in perms:
        print(i)
        break